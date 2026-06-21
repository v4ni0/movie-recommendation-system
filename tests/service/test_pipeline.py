import unittest
import os

from src.service.pipeline import MoviePipeline
from src.config import RAW_DATA_PATH, PROCESSED_DATA_PATH


class TestMoviePipelineRun(unittest.TestCase):

    def setUp(self):
        self.pipeline = MoviePipeline()
        self.test_path = 'data/test_processed.csv'

    def tearDown(self):
        if os.path.exists(self.test_path):
            os.remove(self.test_path)

    def test_run_creates_processed_csv(self):
        df = self.pipeline.run(RAW_DATA_PATH, self.test_path)
        self.assertTrue(os.path.exists(self.test_path))
        self.assertGreater(df.shape[0], 0)
        self.assertIn('content', df.columns)

class TestMoviePipelineBuildIndex(unittest.TestCase):
    def setUp(self):
        self.pipeline = MoviePipeline()
        self.test_index_path = 'data/test_movies_v1.index'

    def tearDown(self):
        if os.path.exists(self.test_index_path):
            os.remove(self.test_index_path)

    def test_build_index_creates_faiss_index(self):
        self.pipeline.build_index(PROCESSED_DATA_PATH, self.test_index_path)
        self.assertTrue(os.path.exists(self.test_index_path))
