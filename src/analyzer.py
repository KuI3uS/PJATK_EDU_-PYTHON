class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def analyze_data(self):
        age_groups = self.data.groupby('Age')['Goals'].mean()
        print(age_groups)

## Użyliśmy pandas do grupowania danych według wieku (metoda groupby) i obliczania średniej liczby goli dla każdej grupy wiekowej