# dag - directed acyclic grapgh

#tasks : 1) fecth AMZN data (extract) 2) clean data (transform) 3) Create and stoee data in table onb postgres (load)
#operators : Python Operator and PostgresOperator
#hooks - allows connection to postgres
#dependencies


from datetime import datetime, timedelta
from airflow import DAG

default_args: dict = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 2, 22),
    'retries':1,
    'retry_delay': timedelta(minutes=5)
    
}


dag = DAG(
    'fetch_and_store_amazon_books',
    default_args=default_args,
    description='A simple DAG to fetch book data from amazon and store it in postgres',
    schedule_interval=timedelta(days=1)
)

