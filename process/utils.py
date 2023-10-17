from os.path import join

from pandas import DataFrame
from yaml import safe_load as yaml_load


def read_cfg(cfg_path: str, key: str = None) -> dict:
    """Read configuration file

    Args:
        cfg_path (str): configuration path

    Returns:
        dict: configuration
    """
    with open(cfg_path, "r") as fid:
        cfg = yaml_load(fid)

    if key is None:
        return cfg

    return cfg[key]


def write_outputs(workdir: str, site_name: str, data: DataFrame):
    """Write outputs from DataFrame to csv

    Args:
        data (DataFrame): data to be converted
    """
    data.to_csv(join(workdir, f"outputs_{site_name}.csv"), index=False)
