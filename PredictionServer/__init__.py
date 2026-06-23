"""PredictionServer package compatibility shim.

This file allows `PredictionServer` to be imported as a package when the
repository is installed. It does not change runtime behaviour of the module
files already present in the directory.
"""
from . import data
from . import predict

__all__ = ["data", "predict"]
