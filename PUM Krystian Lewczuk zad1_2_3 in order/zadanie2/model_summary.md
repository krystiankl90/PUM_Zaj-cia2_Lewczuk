# Model Summary – Zadanie 2 (Titanic)

## Cel
Celem zadania było zbudowanie modelu klasyfikacyjnego przewidującego przeżycie
pasażerów Titanica (zmienna docelowa: Survived).

## Dane
- Dataset: Titanic (train.csv / titanic_prepared)
- Liczba rekordów: 891
- Target: Survived (0/1)

## Przygotowanie danych
- usunięto kolumny: Name, Ticket, Cabin
- uzupełniono brakujące wartości w kolumnie Age medianą
- zmienne kategoryczne zakodowano metodą One-Hot Encoding

## Modele
Przetestowane modele:
- Logistic Regression
- Decision Tree
- Random Forest (Python Recipe)

## Najlepszy model
- Model: Decision Tree
- ROC AUC ≈ 0.89

## Metryki (przykładowe)
- Accuracy ≈ 0.78
- Precision ≈ 0.65
- Recall ≈ 0.93

## Wnioski
Model osiąga dobrą skuteczność w wykrywaniu pasażerów, którzy przeżyli katastrofę,
a zastosowane przygotowanie danych oraz dobór algorytmu istotnie wpływają
na jakość predykcji.
