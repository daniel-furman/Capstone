from argparse import ArgumentParser
import importlib

from transformers import set_seed

from compare_models import compare_models


def main(config):

    set_seed(42)
    compare_models(config["models"], config["input_information"])


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("configs", type=str, help="Config file to set up run pipeline")
    args = parser.parse_args()
    config = importlib.import_module(args.configs).config
    main(config)