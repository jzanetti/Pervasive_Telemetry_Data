from datetime import datetime, timedelta
from os.path import join

from pandas import DataFrame
from yaml import safe_load as yaml_load


def read_cfg(cfg_path: str, realtime_flag: bool, realtime_interval_hr: int = 6) -> dict:
    """Read configuration file

    Args:
        cfg_path (str): configuration path

    Returns:
        dict: configuration
    """
    with open(cfg_path, "r") as fid:
        cfg = yaml_load(fid)

    if realtime_flag:
        cfg["start_datetime"] = datetime.utcnow() - timedelta(hours=realtime_interval_hr)
        cfg["end_datetime"] = datetime.utcnow()

    return cfg


def write_outputs(workdir: str, site_name: str, start_t: str, end_t: str, data: DataFrame):
    """Write outputs from DataFrame to csv

    Args:
        data (DataFrame): data to be converted
    """
    data.to_csv(join(workdir, f"outputs_{site_name}_{start_t}_{end_t}.csv"), index=False)
