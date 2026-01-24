# PUM_Zaj-cia2_Lewczuk
Projekt: Predykcja przeżycia pasażerów Titanica
Model: Decision Tree
Target: Survived (0/1)

Przygotowanie danych:
- Usunięto kolumny: Name, Ticket, Cabin
- Uzupełniono brakujące wartości Age medianą
- Znormalizowano typy danych

Modelowanie:
- Przetestowano Logistic Regression i Decision Tree
- Najlepszy model: Decision Tree (ROC AUC = 0.897)

Metryki:
Accuracy ~ 0.78
Precision ~ 0.65
Recall ~ 0.93
Confusion Matrix dostępna w raporcie modelu.

Zapisany model:
Titanic_Model_Lewczuk

