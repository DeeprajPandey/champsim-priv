#!/usr/bin/env bash

rm -rf bin/

cd script/
./download_dpc3_traces.sh
cd ../

# ./build_champsim.sh bimodal no no no no lru 1
# ./build_champsim.sh bimodal no next_line no no lru 1
# Original Model
./build_champsim.sh bimodal no dbcp dbcp_sup no lru 1
# Keep non-critical misses
./build_champsim.sh bimodal no dbcp no no lru 1

# Our model
./build_champsim.sh bimodal no dbcp_AXR dbcp_sup no lru 1
# Keep non-critical misses
./build_champsim.sh bimodal no dbcp_AXR no no lru 1

# bimodal-no-dbcp_AXR-dbcp_sup-no-lru-1core bimodal-no-dbcp_AXR-no-no-lru-1core
binaries=(bimodal-no-dbcp-dbcp_sup-no-lru-1core bimodal-no-dbcp-no-no-lru-1core)
for bin in "${binaries[@]}"; do
	for trace in dpc3_traces/*; do
		time ./run_champsim.sh $bin 1 5 $(basename $trace)
	done
done

# bimodal-no-no-no-no-lru-1core