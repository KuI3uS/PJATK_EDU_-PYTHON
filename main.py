from src.data_processor import DataLoader, DataManipulator
from src.visualizer import DataVisualizer
from src.analyzer import DataAnalyzer
from src.exception_handler import ExceptionHandler


def main():
    try:
        # Wczytanie danych
        loader = DataLoader('data/euro2024_players.csv')
        loader.load_data()

        # Eksploracja danych
        loader.explore_data()

        # Manipulacja danymi
        manipulator = DataManipulator(loader.data)
        data = manipulator.manipulate_data()

        # Wizualizacja danych
        visualizer = DataVisualizer(data)
        visualizer.visualize_data()

        # Analiza danych
        analyzer = DataAnalyzer(data)
        analyzer.analyze_data()

    except Exception as e:
        ExceptionHandler.handle_exceptions(e)


if __name__ == "__main__":
    main()