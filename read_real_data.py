
import csv
import json
from datetime import datetime, timezone

# Clear the output file ONCE, before processing
open("bidmc_real_data.jsonl", "w").close()

with open("bidmc_01_DATA.csv", newline="") as file:
    reader = csv.DictReader(file)

    for i, row in enumerate(reader):
        row = {
            key.strip(): value.strip()
            for key, value in row.items()
        }

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

        with open("bidmc_real_data.jsonl", "a") as output:
            output.write(json.dumps(data) + "\n")

        if i == 4:
            break

print("Success: 5 real recorded measurements saved!")
