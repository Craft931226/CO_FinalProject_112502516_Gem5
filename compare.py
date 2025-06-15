import re
from collections import defaultdict

files = {"LRU":"Q4_LRU_stats.txt", "LFU":"Q4_LFURP_stats.txt"}
data = defaultdict(dict)

for policy, fname in files.items():
    with open(fname) as f:
        for line in f:
            if "system.l3.overall_miss_rate" in line:
                data[policy]["miss_rate"] = float(line.split()[1])
            if "system.l3.replacements" in line:
                data[policy]["replacements"] = int(line.split()[1])

print(f"{'Metric':<25}{'LRU':>10}{'LFU':>10}{'Diff':>10}")
for key in ["miss_rate","replacements"]:
    lru = data["LRU"][key]
    lfu = data["LFU"][key]
    diff = lfu - lru
    print(f"{key:<25}{lru:>10}{lfu:>10}{diff:>10}")
