import pandas as pd
import random
from datetime import datetime, timedelta
num_samples = 90  
base_time = datetime.now()
def generate_entry(label):
    timestamp = (base_time + timedelta(seconds=random.randint(0, 10000))).strftime('%Y-%m-%d %H:%M:%S')
    event_type = "Modified"
    path = f"decoy_folder/DecoyFile_{random.randint(1,5)}.txt"
    file_name = path.split("/")[-1]
    ext = ".txt"
    file_size = random.randint(40, 60)

    if label == "normal":
        hash_diff_ratio = round(random.uniform(0.0, 0.1), 4)
    elif label == "suspicious":
        hash_diff_ratio = round(random.uniform(0.2, 0.6), 4)
    elif label == "ransomware":
        hash_diff_ratio = round(random.uniform(0.9, 1.0), 4)

    return [timestamp, event_type, path, file_name, ext, file_size, hash_diff_ratio, label]
data = []
for label in ["normal", "suspicious", "ransomware"]:
    for _ in range(num_samples // 3):
        data.append(generate_entry(label))
random.shuffle(data)
df = pd.DataFrame(data, columns=[
    "timestamp", "event_type", "path", "file_name", "ext",
    "file_size", "hash_diff_ratio", "Label"
])
df.to_csv("dummy_dataset.csv", index=False)
print("dummy_dataset.csv created with", len(df), "rows")
