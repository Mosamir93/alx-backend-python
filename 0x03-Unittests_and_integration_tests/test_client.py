#!/usr/bin/env python3
"""Client.py test module."""
import unittest
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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
