import pysparql_anything as sa

engine = sa.SparqlAnything()

microbatching = False

if microbatching == True:
	for n in range(len(os.listdir("./data/acceslibre"))):
		engine.run(
			query="queries/populateOntologyAcceslibre.ttl",
			format="ttl",
			values={
				"filePath": f"data/acceslibre/results-acceslibre-{n}.csv",
			},
			output=f"./data/output-acceslibre-{n}.ttl"
		)

else:
    engine.run(
        query="queries/populateOntologyAcceslibre.ttl",
        format="ttl",
        values={
            "filePath": f"data/acceslibre/results-acceslibre-0.json",
        },
        output=f"data/acceslibre/output-acceslibre-0.ttl"
    )