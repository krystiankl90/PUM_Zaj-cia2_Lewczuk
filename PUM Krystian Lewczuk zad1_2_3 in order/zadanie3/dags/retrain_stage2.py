from airflow.decorators import dag, task
from pendulum import datetime

@dag(
    schedule=None,
    start_date=datetime(2025, 11, 1),
    catchup=False,
    tags=["retrain"]
)
def retrain_stage2():

    @task
    def ingest_data():
        return "titanic_raw"

    @task
    def split_ab(data):
        return {"A": "aData", "B": "bData"}

    @task
    def train_baseline(split):
        return "baseline_model"

    @task
    def fine_tune(model):
        return "finetuned_model"

    @task
    def evaluate(model):
        return "metrics"

    data = ingest_data()
    split = split_ab(data)
    base = train_baseline(split)
    tuned = fine_tune(base)
    evaluate(tuned)

retrain_stage2()
