datasets = {
    "issa": {
        "type": "rdf",
        "url": "http://localhost:8890/sparql",
        "agrovoc": """
                prefix oa: <http://www.w3.org/ns/oa#>
                prefix skosxl: <http://www.w3.org/2008/05/skos-xl#> 
                SELECT distinct ?article (?uri as ?label) 
                from <http://agrovoc.fao.org/graph> 
                from <http://localhost:8890/graph/thematic-descriptors>
                from <http://localhost:8890/graph/annif-descriptors> 
                WHERE { 
                    ?s oa:hasTarget ?article ; oa:hasBody ?uri . 
                } limit 10000 offset %s
            """,
        "wikidata": "",
    },
    "issa-hal": {
        "type": "rdf",
        "url": "http://data-issa.euromov.fr/sparql",
        "kw": """
                prefix oa: <http://www.w3.org/ns/oa#>
                prefix skosxl: <http://www.w3.org/2008/05/skos-xl#> 
                SELECT distinct ?article ?label
                from <http://data-issa.euromov.fr/graph/document-keywords> 
                WHERE { 
                    ?s oa:hasTarget ?article.
                    ?s oa:hasBody ?uri.
                    ?uri rdf:value ?label. 
                } limit 10000 offset %s
            """,
        "entities": """
                prefix oa: <http://www.w3.org/ns/oa#>
                prefix skosxl: <http://www.w3.org/2008/05/skos-xl#> 
                SELECT distinct ?article ?label 
                # from <http://data-issa.euromov.fr/graph/dbpedia-named-entities> 
                # from <http://data-issa.euromov.fr/graph/wikidata-named-entities> 
                # from <http://data-issa.euromov.fr/graph/dbpedia-spotlight-nes> 
                from <http://data-issa.euromov.fr/graph/entity-fishing-nes> 
                from <http://id.nlm.nih.gov/mesh/graph>
                WHERE { 
                    ?s oa:hasTarget ?article ; oa:hasBody ?uri . 
                    ?uri rdf:value ?label .
                } limit 10000 offset %s
            """,
        "wikidata": "",
    },
    "covid": {
        "type": "rdf",
        "url": "http://covidontheweb.inria.fr/sparql",
        "wikidata": """
            prefix wdt:     <http://www.wikidata.org/prop/direct/>
            prefix schema:  <http://schema.org/>
            prefix oa:      <http://www.w3.org/ns/oa#> 
            prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> 
            prefix dct:     <http://purl.org/dc/terms/> 
            SELECT distinct ?article ?label 
            FROM <http://ns.inria.fr/covid19/graph/entityfishing> 
            FROM named <http://ns.inria.fr/covid19/graph/wikidata-named-entities-full>
            FROM <http://ns.inria.fr/covid19/graph/articles>
            WHERE { 
                ?x schema:about ?article; oa:hasBody ?body. 
                
                GRAPH <http://ns.inria.fr/covid19/graph/wikidata-named-entities-full>{ 
                    ?body rdfs:label ?label. 
                } 
                
                ?article dct:issued ?date; dct:abstract [ rdf:value ?abs ].     
            } 
            LIMIT 10000 OFFSET  %s
        """,
    },
    "crobora": {
        "type": "api",
        "url": "http://dataviz.i3s.unice.fr/crobora-api",
        "labels": [
            "http://dataviz.i3s.unice.fr/crobora-api/cluster/names",
            "http://dataviz.i3s.unice.fr/crobora-api/cluster/names2",
        ],
        "images": "http://dataviz.i3s.unice.fr/crobora-api/search/imagesOR?%s&options=illustration&options=location&options=celebrity&options=event",
    },
}
