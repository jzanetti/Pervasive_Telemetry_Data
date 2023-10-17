# Background
This package is used to query data from https://www.telemetry.net.au/

# How to use the package
This package can be run in any Linux box by:
```
python cli/cli_data.py --workdir /tmp/pts --cfg cfg.yml --api_key xxxxxxx
```
where ``--workdir`` is the directory where all the outputs will be stored, ``--cfg`` is the configuration file path, and ``--api_key`` is the API call key that we want to use.

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