class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def analyze_data(self):
        try:
            age_groups = self.data.groupby('Age')['Goals'].mean()
            print(age_groups)
        except KeyError as e:
            print(f"Błąd: brak kolumny {e} w danych.")
            raise
        except Exception as e:
            print(f"Wystąpił błąd podczas analizy danych: {e}")
            raise

## Użyliśmy pandas do grupowania danych według wieku (metoda groupby) i obliczania średniej liczby goli dla każdej grupy wiekowej