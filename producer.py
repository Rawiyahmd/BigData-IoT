
import json
import os
import time
from kafka import KafkaProducer

DRY_RUN = os.getenv("DRY_RUN", "true").lower() == "true"
TOPIC = "medical_sensors"

if not DRY_RUN:
    producer = KafkaProducer(
        bootstrap_servers=os.getenv(
            "KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"
        ),
        value_serializer=lambda data: json.dumps(data).encode("utf-8")
    )

count = 0

with open("bidmc_real_data.jsonl", "r") as file:
    for line in file:
        data = json.loads(line)

        if DRY_RUN:
            print("Ready to send:", data["patient_id"])
        else:
            producer.send(TOPIC, value=data).get(timeout=10)

        count += 1
        time.sleep(1)

if not DRY_RUN:
    producer.close()

print("Records processed:", count)
