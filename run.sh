#!/usr/bin/env bash

# ./build_champsim.sh bimodal no stream no no lru 1
./build_champsim.sh bimodal no stream no no lru 1

binaries=(bimodal-no-stream-no-no-lru-1core)
for bin in "${binaries[@]}"; do
	for trace in dpc3_traces/*; do
		time ./run_champsim.sh $bin 1 10 $(basename $trace)
	done
done