import unittest
import os
from src.data_processor import DataLoader


class TestDataLoader(unittest.TestCase):
    def test_load_data(self):
        file_path = os.path.join(os.path.dirname(__file__), '../data/euro2024_players.csv')
        loader = DataLoader(file_path)
        loader.load_data()
        self.assertIsNotNone(loader.data)


if __name__ == '__main__':
    unittest.main()
