from airflow import DAG,Dataset
from airflow.decorators import task

from datetime import datetime

my_file = Dataset("/temp/my_file.txt")


with DAG(
    dag_id = "consumer",
    schedule=[my_file],
    start_date = datetime(2025,4,28),
    catchup = False
):
    @task
    def read_dataset():
        with open(my_file.uri,"r") as f:
            print(f.read())
            
    read_dataset()