from SPARQLWrapper import SPARQLWrapper, JSON
from supabase import create_client, Client
import os

SUPABASE_URL = "https://nrjxejxbxniijbmquudy.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5yanhlanhieG5paWpibXF1dWR5Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY3NDMwNTY0NCwiZXhwIjoxOTg5ODgxNjQ0fQ.3u7yTeQwlheX12UbEzoHMgouRHNEwhKmvWLtNgpkdBY"

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

import json

def sparql_harvester():
    dmg_json = []
    sparql = SPARQLWrapper(
        "https://stad.gent/sparql" # set SPARQL endpoint here.
    )
    sparql.setReturnFormat(JSON)

    sparql.setQuery("""
        PREFIX cidoc: <http://www.cidoc-crm.org/cidoc-crm/>
        SELECT DISTINCT ?im
        FROM <http://stad.gent/ldes/dmg>
        WHERE {
            ?o cidoc:P129i_is_subject_of ?im
        }
    """)

    try:
        ret = sparql.queryAndConvert()

        for r in ret["results"]["bindings"]:

            #append uri json manifest.
            uri = r['im']['value']
            dmg_json.append(r)
            print(uri)

            #extract object number
            try:
                on = uri.split("/")
                on = on[-1].split(":")[-1]
                print(on)
                data = supabase.table("dmg_objects_LDES").update({"iiif_manifest": uri}).eq("objectNumber", on).execute()

            except Exception as e:
                print(e)

    except Exception as e:
        print(e)

    return dmg_json


