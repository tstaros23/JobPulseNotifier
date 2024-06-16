import unittest
import requests_mock
from job_pulse.robots import check_robots_txt

class TestRobotsTxt(unittest.TestCase):
    """
    This test ensures that the check_robots_txt function returns true if scraping is allowed on the website.

    Args:
        unittest (TestCase): Base class for unit testing in Python.
    """
    @requests_mock.Mocker()
    def test_robots_txt_allows_root(self, mock):
        """
        Test that check_robots_txt allows scraping the root URL if robots.txt permits it.

        Args:
            mock (requests_mock.Mocker): Mock object to simulate HTTP requests.
        """
        url = 'https://example.com/'
        robots_url = 'https://example.com/robots.txt'
        robots_content = """
        User-agent: *
        Disallow: /private
        Allow: /
        """
        mock.get(robots_url, text=robots_content)
        
        self.assertTrue(check_robots_txt(url))

    @requests_mock.Mocker()
    def test_robots_txt_disallows_private(self, mock):
        url = 'https://example.com/private/page'
        robots_url = 'https://example.com/robots.txt'
        robots_content = """
        User-agent: *
        Disallow: /private
        Allow: /
        """
        mock.get(robots_url, text=robots_content)
        
        self.assertFalse(check_robots_txt(url))

    @requests_mock.Mocker()
    def test_robots_txt_allows_public(self, mock):
        url = 'https://example.com/public/page'
        robots_url = 'https://example.com/robots.txt'
        robots_content = """
        User-agent: *
        Disallow: /
        Allow: /public
        """
        mock.get(robots_url, text=robots_content)
        
        self.assertTrue(check_robots_txt(url))

    @requests_mock.Mocker()
    def test_robots_txt_disallows_all_except_public(self, mock):
        url = 'https://example.com/other/page'
        robots_url = 'https://example.com/robots.txt'
        robots_content = """
        User-agent: *
        Disallow: /
        Allow: /public
        """
        mock.get(robots_url, text=robots_content)
        
        self.assertFalse(check_robots_txt(url))

    @requests_mock.Mocker()
    def test_no_robots_txt(self, mock):
        url = 'https://example.com/page'
        robots_url = 'https://example.com/robots.txt'
        mock.get(robots_url, status_code=404)
        
        self.assertTrue(check_robots_txt(url))

if __name__ == '__main__':
    unittest.main()

