import json

valid = 0
invalid = 0

with open("medical_data.jsonl", "r") as file:
    for line in file:
        try:
            data = json.loads(line)

            if (
                isinstance(data["patient_id"], str)
                and isinstance(data["heart_rate"], int)
                and isinstance(data["body_temperature"], (int, float))
                and isinstance(data["spo2"], int)
                and isinstance(data["respiratory_rate"], int)
            ):
                valid += 1
            else:
                invalid += 1

        except (ValueError, KeyError, TypeError):
            invalid += 1

print("Valid records:", valid)
print("Invalid records:", invalid)