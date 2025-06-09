
from kfp.dsl import ContainerOp

def analyse_op():
    return ContainerOp(
        name="Analysis",
        image="ayman909/ecom-smart:latest",
        command=["python3", "Analyse/simple_analyzer.py"]
    )

