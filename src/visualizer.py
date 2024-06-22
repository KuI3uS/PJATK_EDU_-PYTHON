import matplotlib.pyplot as plt
import seaborn as sns


class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def visualize_data(self):
        try:
            plt.figure(figsize=(10, 6))
            sns.histplot(self.data['Age'], bins=10, kde=True)
            plt.title('Histogram wieku zawodników')
            plt.xlabel('Wiek')
            plt.ylabel('Liczba zawodników')
            plt.show()

            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=self.data, x='Age', y='Goals', hue='MarketValue')
            plt.title('Liczba goli vs Wiek')
            plt.xlabel('Wiek')
            plt.ylabel('Liczba goli')
            plt.show()
        except KeyError as e:
            print(f"Błąd: brak kolumny {e} w danych.")
            raise
        except Exception as e:
            print(f"Wystąpił błąd podczas wizualizacji danych: {e}")
            raise
##tworzy histogram wieku zawodników, a metoda scatterplot tworzy wykres punktowy liczby goli w zależności od wieku.
