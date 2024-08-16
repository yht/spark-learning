from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("NetworkWordCount").getOrCreate()

# Membaca data streaming dari socket
lines = spark.readStream.format("socket").option("host", "localhost").option("port", 8080).load()

# Split setiap baris menjadi kata-kata
words = lines.selectExpr("explode(split(value, ' ')) as word")

# Hitung jumlah kemunculan setiap kata
wordCounts = words.groupBy("word").count()

# Mulai query untuk menulis hasil ke konsol
query = wordCounts.writeStream.outputMode("complete").format("console").start()

query.awaitTermination()
