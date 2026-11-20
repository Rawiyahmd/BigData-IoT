from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("HudiPersistenceTest") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://host.docker.internal:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.secret.key", "MedicalMinio2026!") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .getOrCreate()

path = "s3a://bronze/patient_measurements"

print("VERIFYING PERSISTENT HUDI TABLE...")

df = spark.read.format("hudi").load(path)

df.show(truncate=False)

print("Total measurements:", df.count())
print("PERSISTENCE TEST SUCCESSFUL!")

spark.stop()