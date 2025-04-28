import json
import pathlib
import airflow
import requests
import requests.exceptions as request_exceptions
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import CONSTANT as c
from datetime import date

dag_owner = 'Kendrick'

def _get_pictures():
    pathlib.Path("/tmp/images").mkdir(parents=True,exist_ok=True)
    url = f'https://api.nasa.gov/planetary/apod?api_key={c.API_KEY}'
    response = requests.get(url).json()
    today_image = response['hdurl']
    with open(f'todays_image_{date.today()}.png', 'wb') as f:
        f.write(requests.get(today_image).content)
    

with DAG(
    dag_id = "download_rocket_launches",
    start_date = airflow.utils.dates.days_ago(14),
    schedule= '@daily'
)  as dag : 
    None