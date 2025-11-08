import dataiku
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


input_ds = dataiku.Dataset("titanic_prepared")
df = input_ds.get_dataframe()

cols_to_drop = [c for c in ["Name", "Ticket", "Cabin"] if c in df.columns]
df = df.drop(columns=cols_to_drop)

y = df["Survived"].astype(int)
X = df.drop(columns=["Survived"])

num_cols = [c for c in X.columns if X[c].dtype != "object"]
cat_cols = [c for c in X.columns if X[c].dtype == "object"]

numeric_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("ohe", OneHotEncoder(handle_unknown="ignore"))
])

preprocess = ColumnTransformer([
    ("num", numeric_pipe, num_cols),
    ("cat", categorical_pipe, cat_cols)
])


model = RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1)

pipe = Pipeline([
    ("prep", preprocess),
    ("model", model)
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

pipe.fit(X_train, y_train)


pred = pipe.predict(X_test)


print("=== METRYKI MODELU (PYTHON RECIPE) ===")
print("Accuracy:", round(accuracy_score(y_test, pred), 4))
print("Precision:", round(precision_score(y_test, pred), 4))
print("Recall:", round(recall_score(y_test, pred), 4))
print("Confusion Matrix:\n", confusion_matrix(y_test, pred))

output_df = X_test.copy()
output_df["y_true"] = y_test.values
output_df["y_pred"] = pred

output_ds = dataiku.Dataset("rf_predictions")
output_ds.write_with_schema(output_df)
