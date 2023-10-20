from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from cli.cli_data import main

# Define your Airflow DAG
default_args = {
    "owner": "Sijin Zhang",
    "depends_on_past": False,
    # Start on 27th of June, 2020
    "start_date": datetime(2020, 6, 27),
    "email": ["sijin.zhang@esr.cri.nz"],
    "email_on_failure": ["sijin.zhang@esr.cri.nz"],
    "email_on_retry": False,
    # In case of errors, do one retry
    "retries": 3,
    # Do the retry with 30 seconds delay after the error
    "retry_delay": timedelta(seconds=30),
    # Run once every 15 minutes
    "schedule_interval": "*/15 * * * *",
}


workdir = "/tmp/ptd_data"
cfg = "cfg.yml"
realtime_flag = True

# main(workdir, cfg, "3Y0eC7WevYe1r7gUYPlT4w")

with DAG(
    dag_id="air_quality_data_api",
    default_args=default_args,
    schedule_interval="*/30 * * * *",
    tags=["air_quality_data_api"],
) as dag:
    # Use the PythonOperator to run your custom Python function
    run_aa_script_task = PythonOperator(
        task_id="air_quality_data_api",
        python_callable=main,
        op_args=[workdir, cfg, realtime_flag],
        provide_context=True,  # This allows you to access context variables if needed
    )
