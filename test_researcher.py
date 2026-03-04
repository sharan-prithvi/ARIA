import asyncio
import unittest
import os
from researcher import research_item

class TestResearcher(unittest.TestCase):
    def setUp(self):
        self.test_url = "https://www.boat-lifestyle.com/products/airdopes-381"
    
    def test_research_execution(self):
        try:
            asyncio.run(research_item(self.test_url))
        except Exception as e:
            self.fail(f"Research execution failed with error: {e}")

if __name__ == '__main__':
    unittest.main()