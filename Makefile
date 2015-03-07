t0:
	hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming.jar -D mapreduce.job.reduces=1 -file map.py -mapper map.py -file reduce.py -reducer reduce.py -input Articles  -output WordCount

t1:
	hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming.jar -D mapreduce.job.reduces=1 -file CleanWordCountMap.py -mapper CleanWordCountMap.py -file reduce.py -reducer reduce.py -input Articles  -output CleanWordCount

t2:
	hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming.jar -D mapreduce.job.reduces=1 -file InitialCountMap.py -mapper InitialCountMap.py -file reduce.py -reducer reduce.py -input Articles  -output InitialCountMap

t3:
	hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming.jar -D mapreduce.job.reduces=1 -file TopKMap.py -mapper TopKMap.py -file TopKReduce.py -reducer TopKReduce.py -input Articles  -output TopK

t4:
	hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming.jar -D mapreduce.job.reduces=1 -file InvertedIdxMap.py -mapper InvertedIdxMap.py -file InvertedIdxReduce.py -reducer InvertedIdxReduce.py -input Articles  -output InvertedIndex
