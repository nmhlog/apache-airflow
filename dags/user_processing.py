from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

import json
from pandas import json_normalize

def _process_user(ti):
    user = ti.xcom_pull(task_ids="extract_user")
    user = user["results"][0]
    
    

with DAG( 'user_processing', start_date = datetime(2025,4,22), schedule = '@daily',  catchup = False  ):
    # Corn parameter
    # if airflow was never run will automatically run dag
    create_pet_table = SQLExecuteQueryOperator(
        task_id="create_table",
        conn_id = 'postgres',
        sql="""
            CREATE TABLE IF NOT EXISTS pet (
            pet_id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            pet_type VARCHAR NOT NULL,
            birth_date DATE NOT NULL,
            OWNER VARCHAR NOT NULL);
        """,
            )
    
    is_api_available = HttpSensor(
        task_id='is_api_available',
        http_conn_id="user_api",
        endpoint = "api/"
        
    )
    
    extract_user = SimpleHttpOperator(
        task_id = 'extract_user',
        http_conn_id = 'user_api',
        endpoint = 'api/',
        method = 'GET',
        response_filter = lambda response : json.loads(response.text)
    )
    
    process_user = PythonOperator(
            task_id  ='process_user',
            python_callable=_process_user
    )