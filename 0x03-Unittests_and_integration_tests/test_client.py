#!/usr/bin/env python3
"""Client.py test module."""
import unittest
from unittest.mock import Mock, patch
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
