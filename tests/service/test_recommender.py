import unittest
from src.service.recommender import MovieRecommender

from src.config import RAW_DATA_PATH, PROCESSED_DATA_PATH, INDEX_PATH, MODEL_NAME


class TestMovieRecommenderInit(unittest.TestCase):
    def test_when_valid_paths_provided_then_object_is_successfully_initialized(self):
        recommender = MovieRecommender()
        self.assertIsNotNone(recommender.model)
        self.assertIsNotNone(recommender.index)
        self.assertFalse(recommender.data.empty)

    def test_when_invalid_csv_path_provided_then_throws_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            MovieRecommender(
                original_data_path='data/non_existent.csv',
                processed_data_path='data/non_existent.csv',
                index_path=INDEX_PATH,
            )

    def test_when_invalid_index_path_provided_then_throws_exception(self):
        with self.assertRaises(Exception):
            MovieRecommender(
                processed_data_path=PROCESSED_DATA_PATH,
                index_path='data/wrong_file.index',
            )


class TestMovieRecommenderRecommend(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.recommender = MovieRecommender(
            model_name=MODEL_NAME,
            original_data_path=RAW_DATA_PATH,
            processed_data_path=PROCESSED_DATA_PATH,
            index_path=INDEX_PATH
        )

    def test_recommend_returns_correct_number_of_results(self):
        query = "Space travel and aliens"
        expected_count = 5
        results = self.recommender.recommend(query, top_k=expected_count)
        self.assertEqual(len(results), expected_count)

    def test_recommend_returns_expected_keys(self):
        query = "Romantic comedy"
        expected_keys = ['id', 'title', 'score']
        results = self.recommender.recommend(query)
        self.assertTrue(all(key in results[0] for key in expected_keys))

    def test_recommend_returns_interstellar_when_given_description(self):
        query = "A group of astronauts travels through a wormhole in space in an attempt to ensure humanity's survival."
        results = self.recommender.recommend(query, top_k=1)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], 'Interstellar')
