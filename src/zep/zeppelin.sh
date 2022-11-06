
docker run -u $(id -u) -p 8080:8080 -p 4040:4040 --rm -v $HOME/docker-spark/spark-3.1.3-bin-hadoop2.7:/opt/spark -v $HOME/dev/peps:/dev/peps -v $HOME/dev/buckets:/dev/buckets -e SPARK_HOME=/opt/spark  --name zeppelin apache/zeppelin:0.10.0



