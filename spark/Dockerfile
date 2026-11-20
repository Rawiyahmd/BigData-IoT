
FROM apache/spark:3.5.3-scala2.12-java11-python3-ubuntu

USER root

RUN pip install --no-cache-dir boto3 pandas

# Install S3A connector matching Hadoop 3.3.4
RUN curl -fL \
    https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar \
    -o /opt/spark/jars/hadoop-aws-3.3.4.jar

# AWS SDK required by Hadoop 3.3.4
RUN curl -fL \
    https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar \
    -o /opt/spark/jars/aws-java-sdk-bundle-1.12.262.jar

RUN mkdir -p /home/spark/.ivy2/cache \
    && chown -R spark:root /home/spark/.ivy2 \
    && chmod -R 775 /home/spark/.ivy2

COPY spark-defaults.conf /opt/spark/conf/spark-defaults.conf

USER spark

WORKDIR /opt/spark

CMD ["bash"]
