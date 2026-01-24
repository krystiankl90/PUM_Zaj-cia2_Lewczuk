# Zadanie 1 – Eksploracja danych Titanic (Dataiku DSS)

## 🎯 Cel zadania
Celem zadania było zapoznanie się z podstawami pracy w środowisku Dataiku DSS
oraz przygotowanie prostej eksploracji danych i wizualizacji na zbiorze Titanic,
a następnie udokumentowanie wyników w repozytorium GitHub.

## 📂 Źródło danych
- Dataset: Titanic.csv
- Nazwa w Dataiku: `titanic_raw`
- Liczba rekordów: 891
- Liczba kolumn: 12

## 🔍 Eksploracja danych (Explore)
Zbiór danych zawiera kolumny liczbowe i tekstowe, a wartości brakujące
występują w kolumnach **Age**, **Cabin** oraz **Embarked**.

## 📊 Wykonane wizualizacje
W zakładce Charts przygotowano następujące wykresy:
- histogram wieku pasażerów,
- wykres słupkowy przedstawiający liczbę pasażerów według zmiennej `Survived`,
- wykres słupkowy rozkładu płci (`Sex`),
- wykres pokazujący zależność wieku od przeżycia (`Age` vs `Survived`).

Wszystkie wykresy zostały opublikowane na dashboardzie w Dataiku DSS
oraz zapisane jako obrazy PNG.

## 📌 Wnioski
Największy wpływ na przeżycie pasażerów miały zmienne **Sex**, **Age** oraz **Pclass**.
Z danych wynika, że kobiety przeżywały częściej niż mężczyźni,
a młodsi pasażerowie mieli wyższy odsetek przeżycia niż osoby starsze.

## 📁 Zawartość repozytorium
- `screenshots/` – zrzuty ekranów wykresów i dashboardu,
- `README.md` – opis zadania,
- `raport.md` – odpowiedzi na pytania z kroku 4 zadania.

## ⚠️ Uwagi
Eksport danych do formatu JSON nie był możliwy z powodu ograniczeń uprawnień
w środowisku Dataiku DSS.