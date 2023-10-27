# --------------------
# Conda/mamba environment
# --------------------
override MAMBA = $(CONDA_BASE)/bin/mamba
override CONDA = $(CONDA_BASE)/bin/conda
override PKG = ptd_esr
override CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate


# --------------------
# Airflow environment
# --------------------
AIRFLOW_HOME=/home/zhangs/airflow
AIRFLOW_ENV=/home/zhangs/miniconda3
AIRFLOW_COMMAND=$(AIRFLOW_ENV)/envs/airflow/bin/airflow
AIRFLOW_CONFIG=$(AIRFLOW_HOME)/airflow.cfg
USERNAME ?= szhang
PASSWORD ?= 12345
EMAIL=sijin.zhang@esr.cri.nz

# --------------------
# Package management
# --------------------
clear_env:
	rm -rf $(CONDA_BASE)/envs/$(PKG)
	$(MAMBA) index $(CONDA_BASE)/conda-bld

clear_all:
	rm -rf $(CONDA_BASE)/envs/$(PKG)_env
	rm -rf $(CONDA_BASE)/pkgs/$(PKG)*
	rm -rf $(CONDA_BASE)/conda-bld/linux-64/$(PKG)*
	rm -rf $(CONDA_BASE)/conda-bld/$(PKG)*
	rm -rf $(CONDA_BASE)/conda-bld/linux-64/.cache/paths/$(PKG)*
	rm -rf $(CONDA_BASE)/conda-bld/linux-64/.cache/recipe/$(PKG)*
	$(MAMBA) index $(CONDA_BASE)/conda-bld

env: clear_all
	$(MAMBA) env create -f env.yml
	$(CONDA_ACTIVATE) $(PKG)_env

build:
	$(MAMBA) build .

install: env build
	$(CONDA_ACTIVATE) $(PKG)_env; $(CONDA) install $(PKG) -c local --yes --prefix $(CONDA_BASE)/envs/$(PKG)_env

# --------------------
# Airflow management
# --------------------
create_user:
	$(AIRFLOW_COMMAND) users create --role Admin --username $(USERNAME) --email $(EMAIL) --firstname admin --lastname admin --password $(PASSWORD)

copy_airflow:
	mkdir -p $(AIRFLOW_HOME)/dags
	cp -rf ptd_airflow.py $(AIRFLOW_HOME)/dags/ptd_airflow.py

list_user:
	$(AIRFLOW_COMMAND) users list

db_init:
	export AIRFLOW_HOME=$(AIRFLOW_HOME) && $(AIRFLOW_COMMAND) db init

db_reset:
	$(AIRFLOW_COMMAND) db reset

webserver:
	$(AIRFLOW_COMMAND) webserver -p 8082 >> airflow-webserver.log 2>&1 &

scheduler:
	$(AIRFLOW_COMMAND) scheduler >> airflow-scheduler.log 2>&1 &

worker:
	$(AIRFLOW_COMMAND)  worker

start: copy_airflow db_reset create_user scheduler webserver

end: 
	kill -9 $$(ps aux | grep '[a]irflow' | awk '{print $$2}')
	kill -9 $$(ps aux | grep '[g]unicorn' | awk '{print $$2}')

list_ip:
	netstat -nlp | grep :80
	netstat -nlp | grep :87
	ps aux | grep gunicorn

info:
	$(AIRFLOW_COMMAND) jobs check --job-type SchedulerJob --allow-multiple --limit 100