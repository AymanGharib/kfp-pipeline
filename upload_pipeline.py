import argparse
from kfp import Client

def upload_pipeline(pipeline_path: str, pipeline_name: str):
    client = Client()  # Assumes default endpoint (e.g., localhost:8080 for port-forwarding)
    
    # Upload or update the pipeline
    client.upload_pipeline(
        pipeline_package_path=pipeline_path,
        pipeline_name=pipeline_name
    )
    print(f"✅ Pipeline '{pipeline_name}' uploaded successfully from '{pipeline_path}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload a Kubeflow pipeline YAML.")
    parser.add_argument("--pipeline_path", type=str, required=True, help="Path to the compiled .yaml pipeline file")
    parser.add_argument("--pipeline_name", type=str, required=True, help="Name to register the pipeline under")

    args = parser.parse_args()
    upload_pipeline(args.pipeline_path, args.pipeline_name)
