from pyspark import SparkContext

sc = SparkContext(appName="dcos_hdfs_saveastextfile")
hockeyTeams = sc.parallelize(("wild", "blackhawks", "red wings", "wild", "oilers", "whalers", "jets", "wild"))
hockeyTeams.map(lambda k: (k,1)).countByKey().items()
hockeyTeams.saveAsTextFile("hockey_teams.txt")

