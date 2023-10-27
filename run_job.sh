#!/bin/bash
eval "$(conda shell.bash hook)"
conda activate ptd_esr_env
start_ptd --workdir /tmp/pts3 --cfg /home/zhangs/Github/Pervasive_Telemetry_Data/cfg.yml --realtime_flag
