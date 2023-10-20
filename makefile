AIRFLOW_HOME=/home/zhangs/Github/Pervasive_Telemetry_Data
AIRFLOW_ENV=/home/zhangs/miniconda3
AIRFLOW_COMMAND=$(AIRFLOW_ENV)/envs/airflow/bin/airflow

USERNAME=szhang
PASSWORD=test123
EMAIL=sijin.zhang@esr.cri.nz

create_user:
	$(AIRFLOW_COMMAND) users create --role Admin --username $(USERNAME) --email $(EMAIL) --firstname admin --lastname admin --password $(PASSWORD)

init:
	export AIRFLOW_HOME=$(AIRFLOW_HOME) && $(AIRFLOW_COMMAND) db init

webserver:
	$(AIRFLOW_COMMAND) webserver -p 8082 >> airflow-webserver.log 2>&1 &

scheduler:
	$(AIRFLOW_COMMAND) scheduler

worker:
	$(AIRFLOW_COMMAND) worker

# Start all Airflow components (webserver, scheduler, and worker)
start: webserver scheduler worker

airflow scheduler - DagFileProcessor 