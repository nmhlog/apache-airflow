from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def print_firstdag():
    return 'My First DAG from HevoData!'

dag = DAG('first_dag', description='HevoData Dag',
          schedule_interval='0 8 * * *',
          start_date=datetime(2025, 4, 21), catchup=False)

print_operator = PythonOperator(task_id='first_task', python_callable=print_firstdag, dag=dag)
