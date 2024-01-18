"""
Run the following commands on your machine before executing the code snippet below

sudo apt-get install openjdk-11-jdk-headless -qq > /dev/null
sudo wget -q https://archive.apache.org/dist/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
sudo tar xf spark-3.1.2-bin-hadoop3.2.tgz
pip install -q findspark
"""
import os

# os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"
# os.environ["SPARK_HOME"] = "/home/brainiac/learning/50-algorithms-every-programmer-should-know/spark-3.1.2-bin-hadoop3.2"

import findspark

findspark.init()

from pyspark.sql import SparkSession


spark = SparkSession.builder.master('local[*]').getOrCreate()

sc = spark.sparkContext

words_list = ['python', 'java', 'ottawa', 'ottawa', 'java','news']

words_rdd = sc.parallelize(words_list, 4)

words_pairs = words_rdd.map(lambda w: (w, 1))

word_counts_collected = words_pairs.reduceByKey(lambda x, y: x + y)


if __name__ == '__main__':
    # Print out the type of words_rdd
    print(words_rdd.collect())

    print(words_pairs.collect())

    print(word_counts_collected.collect())
