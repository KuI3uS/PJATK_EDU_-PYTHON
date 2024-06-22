# UEFA EURO 2024 Players Data Analysis

## Opis

Projekt służy do analizy danych zawodników UEFA EURO 2024. Program wczytuje dane, wykonuje podstawowe manipulacje, wizualizuje je oraz generuje wnioski na ich podstawie.

## Instrukcja uruchomienia

1. Upewnij się, że masz zainstalowane wszystkie wymagane biblioteki:
    ```
    pip install -r requirements.txt
    ```

2. Uruchom główny skrypt:
    ```
    python main.py
    ```

### a. Dlaczego zastosowane w programie metody są dostosowane do wybranego typu danych i prezentowanego zagadnienia analitycznego?

- Wczytywanie danych: Użyliśmy pandas do wczytywania i manipulacji danymi, co jest standardem w analizie danych.
- Eksploracja danych: Podstawowe metody eksploracji danych (head, info, describe) pozwalają na szybkie zrozumienie struktury i jakości danych.
- Manipulacja danymi: Filtrowanie i sortowanie danych pozwala na skupienie się na istotnych informacjach.
- Wizualizacja danych: Matplotlib i Seaborn są powszechnie używanymi bibliotekami do tworzenia wykresów, co ułatwia prezentację danych w przystępny sposób.
- Analiza danych: Grupowanie i obliczanie średnich wartości pozwala na wyciągnięcie kluczowych wniosków z danych.

### b. Wyjaśnienie zastosowanych rozwiązań programistycznych

- **Struktura klas**: Projekt wykorzystuje paradygmat programowania obiektowego, co zwiększa czytelność i łatwość konserwacji kodu.
- **Wzorce projektowe**: Użycie wzorców takich jak `DataLoader`, `DataManipulator`, `DataVisualizer` i `DataAnalyzer` pozwala na modularność i łatwość rozbudowy projektu.
- **Standardy kodowania**: Kod jest zgodny z PEP8, co zapewnia jego czytelność i zgodność z najlepszymi praktykami programistycznymi.

## Obsługa wyjątków

- Program zawiera mechanizmy obsługi wyjątków, które zapewniają nieprzerwaną egzekucję, nawet w przypadku błędów takich jak brak pliku czy błędne dane.# PJATK_EDU_-PYTHON
- Każda klasa obsługuje potencjalne wyjątki, które mogą być wywołane przez użytkownika, 