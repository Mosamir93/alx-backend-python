#!/usr/bin/env python3
"""Client.py test module."""
import unittest
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from typing import Dict
from fixtures import TEST_PAYLOAD
from requests import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class definition."""
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json')
    def test_org(self, org: str, mock_json: Mock) -> None:
        """A test for org method."""
        mock_json.return_value = {"payload": True}
        client = GithubOrgClient(org)
        self.assertEqual(client.org, {"payload": True})
        mock_json.assert_called_once_with(client.ORG_URL.format(org=org))

    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    def test_public_repos_url(self, test_org) -> None:
        """A _public_repos_url test method."""
        url = f"https://api.github.com/orgs/{test_org}/repos"
        mock_org_payload = {"repos_url": url}
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = mock_org_payload
            client = GithubOrgClient(test_org)
            self.assertEqual(client._public_repos_url, url)

    @patch('client.get_json')
    def test_public_repos(self, mock_json: Mock) -> None:
        """A unittest for GithubOrgClient.public_repos."""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_repos:
            payload = [{"name": "repo1"}, {"name": "repo2"}]
            mock_json.return_value = payload
            url = "https://api.github.com/orgs/test_org/repos"
            mock_repos.return_value = url
            client = GithubOrgClient("test_org")
            self.assertEqual(client.public_repos(), ["repo1", "repo2"])
            mock_json.assert_called_once_with(url)
            mock_repos.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, license_key: str, expected: bool):
        """A unittest for has_license method."""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class([
        {
            'org_payload': TEST_PAYLOAD[0][0],
            'repos_payload': TEST_PAYLOAD[0][1],
            'expected_repos': TEST_PAYLOAD[0][2],
            'apache2_repos': TEST_PAYLOAD[0][3],
        },
    ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestIntegrationGithubOrgClient class definition."""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()
