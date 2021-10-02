import click
import joblib
import os
from easy_serving.service.model_server.main import run_dev_server


@click.command()
@click.option("-m", "--model_path", type=str, help="Absolute path to the model pkl file.", required=True)
def cli(model_path):
    """Welcome to Easy-Serving! the No. 1 Python Mlops Cli"""
    loaded_model = joblib.load(open(model_path, 'rb'))
    os.environ['MODEL_BASE_PATH'] = model_path
    click.echo("Model Loaded successfully from path")
    run_dev_server()
    pass
