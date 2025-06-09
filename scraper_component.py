from kfp.dsl import ContainerOp

def scraper_op():
    return ContainerOp(
        name="Scraper",
        image="ayman909/ecom-smart:latest",
        command=["python3", "test_agents.py"]
    )

