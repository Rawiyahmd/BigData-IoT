from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("HudiS3UpsertTest") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://host.docker.internal:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.secret.key", "MedicalMinio2026!") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .getOrCreate()

path = "s3a://bronze/patient_measurements"

print("BEFORE UPSERT:")
spark.read.format("hudi").load(path).show()

# Update M001 and insert M005
data = [
    ("M001", "P001", "heart_rate", 95.0, 1700000010),
    ("M005", "P003", "spo2", 97.0, 1700000011)
]

columns = [
    "measurement_id",
    "patient_id",
    "sensor_type",
    "value",
    "ts"
]

df = spark.createDataFrame(data, columns)

hudi_options = {
    "hoodie.table.name": "patient_measurements",
    "hoodie.datasource.write.recordkey.field": "measurement_id",
    "hoodie.datasource.write.precombine.field": "ts",
    "hoodie.datasource.write.partitionpath.field": "patient_id",
    "hoodie.datasource.write.table.type": "COPY_ON_WRITE",
    "hoodie.datasource.write.operation": "upsert",
    "hoodie.datasource.write.hive_style_partitioning": "true"
}

df.write.format("hudi") \
    .options(**hudi_options) \
    .mode("append") \
    .save(path)

print("AFTER UPSERT:")
result = spark.read.format("hudi").load(path)
result.show()

print("UPSERT COMPLETED SUCCESSFULLY!")

spark.stop()