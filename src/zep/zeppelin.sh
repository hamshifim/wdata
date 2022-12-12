
docker run -u $(id -u) -p 8080:8080 -p 4040:4040 --rm -v $HOME/docker-spark/spark-3.1.3-bin-hadoop2.7:/opt/spark -v $HOME/dev/duds/:/dev/duds -v $HOME/dev/buckets:/dev/buckets -e SPARK_HOME=/opt/spark --network host --name zeppelin apache/zeppelin:0.10.0
