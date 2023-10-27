import argparse
from os import makedirs
from os.path import exists

from process.data import create_table, query_data
from process.utils import read_cfg, write_outputs


def get_example_usage():
    example_text = """example:
        * start_ptd --workdir /tmp/pts
                    --cfg pts_sites.cfg
                    [--realtime_flag]
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
    parser.add_argument("--realtime_flag", action="store_true", help="If run the task in realtime")

    return parser.parse_args(
        # ["--workdir", "/tmp/pts", "--cfg", "cfg.yml", "--realtime_flag"]
    )


def main():
    """Main function of data query from Pervasive Telemetry System

    Args:
        workdir (str): Working directory
        cfg (str): Configuration for PTS sites
    """
    args = setup_parser()
    workdir = args.workdir
    cfg = args.cfg
    realtime_flag = args.realtime_flag

    if not exists(workdir):
        makedirs(workdir)

    cfg = read_cfg(cfg, realtime_flag)

    all_outputs = []
    for proc_site in cfg["sites"]:
        proc_output = query_data(
            proc_site,
            cfg["api_code"],
            cfg["start_datetime"],
            cfg["end_datetime"],
            cfg["limit"],
        )

        all_outputs.append(create_table(proc_output, proc_site))

    write_outputs(
        workdir,
        cfg["start_datetime"].strftime("%Y%m%d%H%M"),
        cfg["end_datetime"].strftime("%Y%m%d%H%M"),
        all_outputs,
    )


if __name__ == "__main__":
    main()
