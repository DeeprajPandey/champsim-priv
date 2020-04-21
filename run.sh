#!/usr/bin/env bash

# ./build_champsim.sh bimodal no no no no lru 1
# ./build_champsim.sh bimodal no no no no fifo 1

binaries=(bimodal-no-no-no-no-lru-1core)
for bin in "${binaries[@]}"; do
	for trace in dpc3_traces/*; do
		time ./run_champsim.sh $bin 5 50 $(basename $trace)
	done
done

# bimodal-no-no-no-no-lru-1core