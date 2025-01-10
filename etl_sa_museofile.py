import pysparql_anything as sa

engine = sa.SparqlAnything()

microbatching = True

if microbatching == True:
	for n in range(1,4):
		engine.run(
			query="queries/populateOntology.ttl",
			format="ttl",
			values={
				"filePath": f"data/musees-de-france-base-museofile-{n}.csv",
			},
			output=f"./data/output-{n}.ttl"
		)

# else:
# 	engine.run(
# 			query="queries/populateOntology.ttl",
# 			format="ttl",
# 			values={
# 				"filePath" : "data/musees-de-france-base-museofile.csv",
# 				"fileName" : "musees-de-france-base-museofile"
# 			},
# 			output="./data/output.ttl"
# 		)


