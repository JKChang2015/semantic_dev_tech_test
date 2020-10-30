from neo4j import GraphDatabase
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("OWL_file_url")
args = parser.parse_args()

conf = "https://raw.githubusercontent.com/VirtualFlyBrain/neo4j2owl/" \
       "master/src/test/resources/minimal-config.yaml"

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "neo4j"))
statement = "CALL ebi.spot.neo4j2owl.owl2Import('$owl_file','$conf')"

with driver.session() as session:
    session.run(statement, conf=conf, owl_file=args.OWL_file_uri)

