import pandas as pd
import random

rows = []

# generate normal logs
for _ in range(500):
    rows.append([
        "2025-01-01 12:00",
        "10.0.0." + str(random.randint(1,10)),
        "10.0.0." + str(random.randint(11,20)),
        random.randint(300,3000),    # bytes
        random.randint(1,25),        # packets
        random.uniform(0.5,5)        # duration
    ])

# generate anomalies
for _ in range(25):
    rows.append([
        "2025-01-01 12:00",
        "10.0.0." + str(random.randint(1,10)),
        "10.0.0." + str(random.randint(11,20)),
        random.randint(50000,900000),   # HIGH bytes
        random.randint(200,8000),       # HIGH packets
        random.uniform(20,80)           # LONG duration
    ])

df = pd.DataFrame(rows, columns=["timestamp","src_ip","dst_ip","bytes","packets","duration"])
df.to_csv("data/network_logs.csv", index=False)

print("Logs generated!")