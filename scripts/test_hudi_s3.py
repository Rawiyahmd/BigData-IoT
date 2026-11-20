from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("HudiS3Test") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://host.docker.internal:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.secret.key", "MedicalMinio2026!") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .getOrCreate()

print("Creating patient measurements...")

data = [
    ("M001", "P001", "heart_rate", 82.0, 1700000001),
    ("M002", "P001", "spo2", 98.0, 1700000002),
    ("M003", "P002", "heart_rate", 75.0, 1700000003),
    ("M004", "P002", "temperature", 36.7, 1700000004)
]

columns = [
    "measurement_id",
    "patient_id",
    "sensor_type",
    "value",
    "ts"
]

df = spark.createDataFrame(data, columns)

df.show()

print("Writing Hudi table to Bronze...")

hudi_options = {
    "hoodie.table.name": "patient_measurements",
    "hoodie.datasource.write.recordkey.field": "measurement_id",
    "hoodie.datasource.write.precombine.field": "ts",
    "hoodie.datasource.write.partitionpath.field": "patient_id",
    "hoodie.datasource.write.table.type": "COPY_ON_WRITE",
    "hoodie.datasource.write.operation": "upsert",
    "hoodie.datasource.write.hive_style_partitioning": "true"
}

df.write \
    .format("hudi") \
    .options(**hudi_options) \
    .mode("append") \
    .save("s3a://bronze/patient_measurements")

print("Hudi table written successfully!")

print("Reading Hudi table back...")

df2 = spark.read \
    .format("hudi") \
    .load("s3a://bronze/patient_measurements")

df2.show()

print("SUCCESS: Hudi + S3 + Bronze working!")

spark.stop()