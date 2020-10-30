# Semantic Dev Tech Test  [![Build Status](https://travis-ci.org/EBISPOT/semantic_dev_tech_test.svg?branch=master)](https://travis-ci.org/EBISPOT/semantic_dev_tech_test)

Technical test for semantic dev.

This GitHub Repository has:

 *  An OWL file with an ontology/KnowledgeBase of wines (src/resources/wine.owl)
 *  A `.travis.yml` file that launches a containerised Neo4j DataBase with a representation of the ontology/knowledgeBase
 

### Excercise 1:

Explore the OWL file in Protege and run a reaonser.

![image](https://user-images.githubusercontent.com/112839/97699007-60bd2f00-1aa1-11eb-8e1a-ab8a5b1c98ac.png)

Please explain, in clear English, why the reasoner classifies Barolo as an Italian wine.

Launch a local copy of the DB and load the ontology

```sh
docker run -p:7474:7474 -p 7687:7687 --env-file ./src/resources/env.list matentzn/vfb-prod
python src/load_db.py <OWL FILE URL>
```

You should be able to browse at http://localhost:7474

Please write concise documentation summarising the transformation of OWL to Neo4j.

### Excercise 2: 

Using a forked copy of this Repo as a base, write an API library to query the DataBase with methods to:

* List all grape growing regions (in the ontology)
* List all varietals  (in the ontology)
* List all types (classes) of wine  (in the ontology)
* Query for wine types and individual wines by: colour, varietal, region

Your code should:
  * be in Python
  * have unit tests with continuous integration via Travis or GitHub Actions
  * be well documented

If you prefer, you may base your API on SPARQL queries of the ontology/KnowledgeBase in place of Cypher queries of the Neo4J DataBase.

You should include clear documentation on how to use your API.

### Excercise 3:

Write a couple of paragraphs on how you might extend the OWL modelling and content to build a KnowledgeBase of individual wines that would be useful to consumers trying to decide what wine to buy.
