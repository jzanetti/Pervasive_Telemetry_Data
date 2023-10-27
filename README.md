# Background
This package is used to query data from https://www.telemetry.net.au/

# Installation
The package can be installed via: 
```
make install
``` 
After the installation, an environment called ``ptd_esr_env`` is created and the package ``ptd_esr`` is installed under this package.

# How to run the package
This package can be run in any Linux box by:
```
conda activate ptd_esr_env
python start_ptd --workdir /tmp/pts --cfg cfg.yml --realtime_flag
```
where ``--workdir`` is the directory where all the outputs will be stored, ``--cfg`` is the configuration file path, and ``--realtime_flag`` is a flag whether we run the job in realtime

# Run airflow:
The airflow job can be triggered as:

- Step 1: activate the environment: ``conda activate ptd_esr_env``
- Step 2 (option): initialize a airflow database ``make init``
- Step 3: start airflow: ``make start``
- Step 4: end airflow: ``make end``

Note that the following ports/URL are pre-defined in the airflow:

- endpoint_url: ``http://localhost:8082``
- worker_log_server_port: ``8083``
- web_server_port: ``8082``

Other useful commands include:

- Create a new users: ``export USERNAME=szhang; export PASSWORD=12345; make create_user`` 
- List all users: ``make list_user``
- List all used ports: ``make list_ip``

# Configuration:
The configuration file must be provided, a sample configuration file is provided below:
```
start_datetime: 2023-09-18T08:20:00Z
end_datetime: 2023-10-18T08:20:00Z

limit: 100

sites:
  - 10298
```
Here it includes the time span for the data, the maximum reports we want to extract, and the site number that we want to extract.

