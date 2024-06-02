import unittest
from job_pulse.app import scrape_jobs
from unittest.mock import patch

class TestScrapeJobs(unittest.TestCase):

    @patch('job_pulse.app.requests.get')  # Mock 'requests.get' in the correct module
    def test_scrape_jobs_with_sample_data(self, mock_get):
        # Sample HTML data
        sample_html = """
        <div id="text-353cc9e8aa">
            <h5>Job Title 1</h5>
            <h5>Job Title 2</h5>
            <h5>Job Title 3</h5>
        </div>
        """
        
        # Configure the mock to return a response with the sample HTML
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = sample_html
        
        # Call the function to test
        jobs = scrape_jobs()
        
        # Assert the expected output
        expected_jobs = ["Job Title 1", "Job Title 2", "Job Title 3"]
        self.assertEqual(jobs, expected_jobs)

if __name__ == '__main__':
        print("Python interpreter:", sys.executable)  # Print the Python interpreter being used
        unittest.main()
