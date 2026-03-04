import unittest
import os
from pipeline import run_pipeline

class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.image_path = 'test1.jpg'
        if not os.path.exists(self.image_path):
            self.skipTest(f"Test image '{self.image_path}' not found. Please add it to run the test.")
    
    def test_pipeline_execution(self):
        try:
            run_pipeline(self.image_path)
        except Exception as e:
            self.fail(f"Pipeline execution failed with error: {e}")

if __name__ == '__main__':
    unittest.main()