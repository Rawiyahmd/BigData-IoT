import random
import json
import uuid
import time
from datetime import datetime, timezone

patients = {
    "PATIENT_01": "Room A",
    "PATIENT_02": "Room B",
    "PATIENT_03": "Room C",
    "PATIENT_04": "Room D",
    "PATIENT_05": "Room E"
}

with open("medical_data.jsonl", "w") as file:
    for i in range(50):
        patient = random.choice(list(patients))

        data = {
            "record_id": str(uuid.uuid4()),
            "patient_id": patient,
            "sensor_id": "SENSOR_" + patient[-2:],
            "heart_rate": random.randint(60, 120),
            "body_temperature": round(random.uniform(36, 39), 2),
            "spo2": random.randint(90, 100),
            "respiratory_rate": random.randint(12, 25),
            "location": patients[patient],
            "event_time": datetime.now(timezone.utc).isoformat()
        }

        file.write(json.dumps(data) + "\n")
        file.flush()

        print(json.dumps(data))
        time.sleep(1)

print("Success: 50 medical records saved!")