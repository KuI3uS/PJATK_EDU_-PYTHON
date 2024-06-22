import pandas as pd


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
        except FileNotFoundError:
            print(f"Plik {self.file_path} nie został znaleziony.")
            raise
        except pd.errors.EmptyDataError:
            print("Plik jest pusty.")
            raise
        except Exception as e:
            print(f"Wystąpił błąd: {e}")
            raise
## Wczytywanie danych: Użyliśmy pandas do wczytywania danych z pliku CSV do obiektu DataFrame, co jest standardem w analizie danych. Metoda read_csv jest wywoływana wewnątrz bloku try-except w celu obsługi potencjalnych błędów związanych z brakiem pliku, pustym plikiem lub innymi wyjątkami.
    def explore_data(self):
        if self.data is not None:
            print(self.data.head())
            print(self.data.info())
            print(self.data.describe())
        else:
            print("Dane nie zostały wczytane.")

##Eksploracja danych: Metoda explore_data używa funkcji head(), info() i describe() z biblioteki pandas, aby wyświetlić pierwsze kilka wierszy danych.
class DataManipulator:
    def __init__(self, data):
        self.data = data

    def manipulate_data(self):
        self.data['Age'] = self.data['Age'].astype(int)
        filtered_data = self.data[self.data['Age'] > 30]
        sorted_data = filtered_data.sort_values(by='Goals', ascending=False)
        return sorted_data
##Manipulacja danymi: Używamy pandas do konwersji typów danych (metoda astype), filtrowania danych