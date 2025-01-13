import pysparql_anything as sa

engine = sa.SparqlAnything()

microbatching = True

if microbatching == True:
	for n in range(1,4):

		text_to_replace = "./data/musees-de-france-base-museofile.csv"
		text_replacing = f"./data/musees-de-france-base-museofile-{n}.csv"

		with open("./queries/populateOntologyMuseofile.ttl", 'r') as f:
			filedata = f.read()
			filedata.replace(text_to_replace, text_replacing)

		engine.run(
			query="queries/populateOntologyMuseofile.ttl",
			format="ttl",
			values={
				"filePath": f"data/musees-de-france-base-museofile-{n}.csv",
				"fileName": f"data/musees-de-france-base-museofile-{n}"
			},
			output=f"./data/output-museofile-{n}.ttl"
		)

else:
	engine.run(
			query="queries/populateOntology.ttl",
			format="ttl",
			values={
				"filePath" : "data/musees-de-france-base-museofile.csv",
				"fileName" : "musees-de-france-base-museofile"
			},
			output="./data/output-museofile.ttl"
		)


