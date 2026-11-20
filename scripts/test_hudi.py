
from pyspark.sql import SparkSession

# 1. Create Spark session
spark = (
    SparkSession.builder
    .appName("MedicalMonitoringHudiTest")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

# 2. Create sample medical measurements
data = [
    ("M001", "P001", 82, 36.8, 98, 1732107600, "2026-11-20"),
    ("M002", "P002", 75, 37.0, 97, 1732107660, "2026-11-20"),
    ("M003", "P001", 88, 36.9, 96, 1732107720, "2026-11-20")
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

df = spark.createDataFrame(data, columns)

# 3. Define Hudi table
table_name = "patient_measurements"
table_path = "/tmp/hudi_patient_test"

hudi_options = {
    "hoodie.table.name": table_name,
    "hoodie.datasource.write.table.type": "COPY_ON_WRITE",
    "hoodie.datasource.write.recordkey.field": "measurement_id",
    "hoodie.datasource.write.precombine.field": "event_time",
    "hoodie.datasource.write.partitionpath.field": "measurement_date",
    "hoodie.datasource.write.operation": "upsert"
}

# 4. Write data into Hudi
df.write.format("hudi") \
    .options(**hudi_options) \
    .mode("overwrite") \
    .save(table_path)

print("Hudi table created successfully!")

# 5. Read the Hudi table
result = spark.read.format("hudi").load(table_path)

print("Reading Hudi table:")
result.select(
    "measurement_id",
    "patient_id",
    "heart_rate",
    "temperature",
    "spo2"
).show()

spark.stop()
