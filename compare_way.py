import re
from collections import defaultdict

files = {"2way":"Q3_2way_stats.txt", "fullway":"Q3_fullWay_stats.txt"}
data = defaultdict(dict)

for policy, fname in files.items():
    with open(fname) as f:
        for line in f:
            if "system.l3.overall_miss_rate" in line:
                data[policy]["miss_rate"] = float(line.split()[1])
            # if "system.cpu.dcache.replacements" in line:
            #     data[policy]["replacements"] = int(line.split()[1])

print(f"{'Metric':<25}{'twoway':>10}{'fullway':>10}{'Diff':>10}")
for key in ["miss_rate",
            # "replacements"
            ]:
    twoway = data["2way"][key]
    fullway = data["fullway"][key]
    diff = twoway - fullway
    print(f"{key:<25}{twoway:>10}{fullway:>10}{diff:20}")
