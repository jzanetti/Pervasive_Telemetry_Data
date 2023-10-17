import argparse
from os import makedirs
from os.path import exists

from process.data import create_table, query_data
from process.utils import read_cfg, write_outputs


def get_example_usage():
    example_text = """example:
        * cli_data --workdir /tmp/pts
                   --cfg pts_sites.cfg
                   --api_key xxxxx123
        """
    return example_text


def setup_parser():
    parser = argparse.ArgumentParser(
        description="Querying data from Pervasive Telemetry System",
        epilog=get_example_usage(),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--workdir", required=True, help="Working directory, e.g., where the output will be stored"
    )

    parser.add_argument("--cfg", required=True, help="Configuration path")
    parser.add_argument("--api_key", required=True, help="API key value")

    return parser.parse_args()


def main(workdir: str, cfg: str, api_key: str):
    """Main function of data query from Pervasive Telemetry System

    Args:
        workdir (str): Working directory
        cfg (str): Configuration for PTS sites
        api_key (str): API key to be used
    """
    if not exists(workdir):
        makedirs(workdir)

    cfg = read_cfg(cfg)
    for proc_site in cfg["sites"]:
        proc_output = query_data(
            proc_site, api_key, cfg["start_datetime"], cfg["end_datetime"], cfg["limit"]
        )
        write_outputs(workdir, proc_site, create_table(proc_output))


if __name__ == "__main__":
    args = setup_parser()
    main(args.workdir, args.cfg, args.api_key)
