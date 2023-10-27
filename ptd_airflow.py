from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "Sijin",
    "depends_on_past": False,
    "start_date": datetime(2023, 10, 26),
    "email": ["sijin.zhang@esr.cri.nz"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG("call_ptd", default_args=default_args, schedule_interval=timedelta(hours=6))

t1 = BashOperator(
    task_id="ptd_job",
    bash_command="/home/zhangs/Github/Pervasive_Telemetry_Data/run_job.sh ",
    # bash_command='echo "hello world";',
    dag=dag,
)
