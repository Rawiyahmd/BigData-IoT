
import csv
import json
from datetime import datetime, timezone

count = 0
skipped = 0

with open("bidmc_01_DATA.csv", newline="") as file:
    reader = csv.DictReader(file)

    with open("bidmc_real_data.jsonl", "w") as output:
        for i, row in enumerate(reader):

            # Remove spaces from column names and values
            row = {
                key.strip(): value.strip()
                for key, value in row.items()
            }

            # Skip incomplete measurements
            if any(
                row[column].lower() in ("nan", "")
                for column in ["HR", "PULSE", "RESP", "SpO2"]
            ):
                skipped += 1
                continue

            data = {
                "record_id": f"BIDMC_01_{i}",
                "patient_id": "BIDMC_01",
                "heart_rate": int(row["HR"]),
                "pulse_rate": int(row["PULSE"]),
                "respiratory_rate": int(row["RESP"]),
                "spo2": int(row["SpO2"]),
                "time_seconds": int(row["Time [s]"]),
                "event_time": datetime.now(timezone.utc).isoformat(),
                "source": "BIDMC_recorded_data"
            }

            output.write(json.dumps(data) + "\n")
            count += 1

print("Valid records saved:", count)
print("Incomplete records skipped:", skipped)
