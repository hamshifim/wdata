Installation Instructions
=

1. Make sure you have $HOME/dev/<super project>
2. Make sure you have $HOME/dev/buckets
3. Create a directory $HOME/docker-spark
4. Download (wget) https://downloads.apache.org/spark/spark-3.1.3/spark-3.1.3-bin-hadoop2.7.tgz
5. `docker run -u $(id -u) -p 8080:8080 -p 4040:4040 --rm -v $HOME/docker-spark/spark-3.1.3-bin-hadoop2.7:/opt/spark -v $HOME/dev/peps:/dev/peps -v $HOME/dev/buckets:/dev/buckets -e SPARK_HOME=/opt/spark  --name zeppelin apache/zeppelin:0.10.0`

Intellij
=
Open module setting and add module dependencies:
1. Wielder
2. Wild
3. CassandraPipe
4. KafkaIngestion

Running JAR in Console
=
1. In local cmd run:
   1. `$HOME/dev/<super project>/PepSpark/build.sh`
   2. `$HOME/dev/<super project>/Pipelines/datalake/CassandraPipe/build.sh`
   3. `$HOME/dev/<super project>/Pipelines/datalake/KafkaIngestion/build.sh`
2. Go To Zeppelin GUI at localhost:8080
3. On the top right click the dropdown (anonymous or some other name) and choose interpreter
4. Search for spark and click edit
5. In spark.jars paste (the directories should be mounted):
/dev/peps/Pipelines/datalake/CassandraPipe/target/CassandraPipe-1.0.0-SNAPSHOT-jar-with-dependencies.jar,/dev/peps/Pipelines/datalake/KafkaIngestion/target/KafkaIngestion-1.0.0-SNAPSHOT-jar-with-dependencies.jar,/dev/peps/PepSpark/target/PepSpark-1.0.0-SNAPSHOT-jar-with-dependencies.jar
6. Click save
7. Check by adding the below import statement to a zeppelin notebook:
`
   import com.pepticom.wielder.wild.{FsUtil, SparkContextInitializer}
   import com.typesafe.config.Config
   import org.apache.spark.sql.{DataFrame, SparkSession}
`

Connect to remote Zeppelin(on AWS) from IntelliJ Idea
=
1. Create SSH tunnel to bastion instance(manually or using script)
2. Open notebook or IntelliJ settings and find `Big Data Tools`
3. Add new zeppelin notebook
4. Copy URL from AWS console in `Applications` tab for Zeppelin, and paste to `URL` into IntelliJ
5. In IntelliJ activate `Enable tunneling` option and click on `...`
6. In new open window add new config
7. Copy URL of `Master public DNS` on `Summary`(main) tab and paste as host
8. Add username `hadoop`(it always left the same)
9. Change `Authentication type` from Password to `Key pair OpenSSH or PuTTY`
10. Specify path to private key file(that was created with terraform) for that EMR cluster(specific environment)
11. In Connection parameters, activate option to `Send keep-alive messages every ... seconds` and change from 300 to 5
12. In `HTTP/SOCKS proxy` select SOCKS proxy
13. In hostname write `127.0.0.1`
14. In port write `8157`(or another port, that used for tunnel)
15. Test connection and apply