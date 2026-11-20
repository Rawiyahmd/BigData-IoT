from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("S3ConnectionTest") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://host.docker.internal:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.secret.key", "MedicalMinio2026!") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .getOrCreate()

print("Testing S3 connection...")

hadoop_conf = spark.sparkContext._jsc.hadoopConfiguration()

fs = spark._jvm.org.apache.hadoop.fs.FileSystem.get(
    spark._jvm.java.net.URI("s3a://bronze/"),
    hadoop_conf
)

print("S3 connection successful!")

path = spark._jvm.org.apache.hadoop.fs.Path("s3a:/")
print("S3 root accessible:", fs.exists(path))

spark.stop()