import random
import json
import uuid
from datetime import datetime, timezone

sensors = {
    "SENSOR_01": "Zone A",
    "SENSOR_02": "Zone B",
    "SENSOR_03": "Zone C",
    "SENSOR_04": "Zone D",
    "SENSOR_05": "Zone E"
}

with open("sensor_data.jsonl", "w") as file:
    for i in range(50):
        sensor = random.choice(list(sensors))

        data = {
            "record_id": str(uuid.uuid4()),
            "sensor_id": sensor,
            "temperature": round(random.uniform(20, 40), 2),
            "humidity": round(random.uniform(30, 80), 2),
            "location": sensors[sensor],
            "event_time": datetime.now(timezone.utc).isoformat()
        }

        file.write(json.dumps(data) + "\n")

print("Success: 50 records from 5 possible sensors!")