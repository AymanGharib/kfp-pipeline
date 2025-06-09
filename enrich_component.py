from kfp.dsl import ContainerOp

def enrich_op():
    return ContainerOp(
        name="LLM Enrichment",
        image="ayman909/ecom-smart:latest",
        command=["python3", "test_llm_enricher.py"]
    )

