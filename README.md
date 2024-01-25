# GUESs: Graph-aware Unsupervised Entity Summarisation


## Abstract

Entity summarisation aims to find a succinct description of an entity (e.g., Germany). This problem arises in disparate areas, such as medicine, in which a doctor requires a quick glimpse to patients having large medical records. Entities form large knowledge graphs with billions of entities and  relationships among them (e.g., Berlin capital of Germany). Each entity description can include hundreds of relationships, many of which are redundant. Extant entity summarisation methods maximize ad hoc measures of interestingness and diversity. Yet, these measures disregard the knowledge graph structure and the local connections around an entity. 

To circumvent this limitation, we introduce GUESs, a Graph-Aware Unsupervised Entity Summarisation method that defines an appropriate interesting measure rooted on graph theoretical concepts. Our method scales to large graph and attains state-of-the-art F1 score on the established Entity Summarisation Benchmark (ESBM). In addition, to measure the impact of the graph structure, we propose ESBM+, an augmentation of ESBM including the missing relationships among entities. GUESs surpasses previous methods on ESBM and increases the advantage with graph-agnostic methods on ESBM+.  


## Install

```
pip3 install numpy==1.21.1
pip3 install sklearn
pip3 install torch==1.12.0
pip3 install pykeen==1.8.2
pip3 install scipy==1.7.1
```

## Run the experiments

```
  # k: Number of cluster
  # m: Fuzzy parameter
  
  # Get the result for GUESs on ESBM
    for k in ks:
        for m in ms:
            get_res("dbpedia", k, m, "transe")
            get_res("lmdb", k, m, "transe")


    # Get the result for GUESs-hard on ESBM
    for k in ks:
        for m in ms:
            get_res_k_means("dbpedia")
            get_res_k_means("lmdb")


    # Get the result for GUESs on ESBM+
    for k in ks:
        for m in ms:
            get_complete_result("dbpedia", k, m, "transe")
            get_complete_result("lmdb", k, m, "transe")

```