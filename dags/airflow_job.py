"""
Code that goes along with the Airflow tutorial located at:
https://github.com/apache/airflow/blob/master/airflow/example_dags/tutorial.py
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('airflow_job', default_args=default_args, schedule_interval=timedelta(days=1))

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='transform_prev_data',
    bash_command='venv/bin/python3 transform_prev_data.py',
    dag=dag)

t2 = BashOperator(
    task_id='transform_ext_data',
    bash_command='venv/bin/python3 transform_ext_data.py',
    retries=3,
    dag=dag)

t3 = BashOperator(
    task_id='merge_features',
    bash_command='venv/bin/python3 merge_features.py',
    retries=3,
    dag=dag)


t4 = BashOperator(
    task_id='train_model',
    bash_command='venv/bin/python3 train_model.py',
    retries=3,
    dag=dag)


t2.set_upstream(t1)
t3.set_upstream(t2)
t4.set_upstream(t3)
