
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("MedicalHudiUpsertTest")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

table_name = "patient_measurements"
table_path = "/tmp/hudi_patient_test"

# New data: M001 is updated, M004 is new
updated_data = [
    ("M001", "P001", 95, 36.9, 97, 1732107800, "2026-11-20"),
    ("M004", "P003", 78, 37.1, 98, 1732107900, "2026-11-20")
]

columns = [
    "measurement_id",
    "patient_id",
    "heart_rate",
    "temperature",
    "spo2",
    "event_time",
    "measurement_date"
]

df = spark.createDataFrame(updated_data, columns)

hudi_options = {
    "hoodie.table.name": table_name,
    "hoodie.datasource.write.table.type": "COPY_ON_WRITE",
    "hoodie.datasource.write.recordkey.field": "measurement_id",
    "hoodie.datasource.write.precombine.field": "event_time",
    "hoodie.datasource.write.partitionpath.field": "measurement_date",
    "hoodie.datasource.write.operation": "upsert"
}

# Update existing record and insert new record
df.write.format("hudi") \
    .options(**hudi_options) \
    .mode("append") \
    .save(table_path)

# Read updated table
result = spark.read.format("hudi").load(table_path)

print("UPDATED HUDI TABLE:")

result.select(
    "measurement_id",
    "patient_id",
    "heart_rate",
    "temperature",
    "spo2"
).orderBy("measurement_id").show()

print("Total records:", result.count())

spark.stop()
