from kfp.compiler import Compiler
from pipeline import smart_pipeline

Compiler().compile(pipeline_func=smart_pipeline, package_path="smart_pipeline.yaml")

