"""Netsolp package initializer.

This module re-exports convenient functions from the project's modules so you
can `import netsolp` and access common utilities.
"""
# The repository contains a few top-level packages (PredictionServer, TrainAndTest)
# that are not nested under the `netsolp` namespace. Import them using absolute
# imports and expose a small, stable surface on `netsolp` for convenience.
try:
    import PredictionServer as PredictionServer
    import PredictionServer.predict as prediction
    from PredictionServer.predict import get_preds, get_preds_distilled
    from PredictionServer.data import read_fasta, FastaBatchedDataset, BatchConverter
except Exception:
    # Avoid import-time failures if optional heavy dependencies are missing.
    PredictionServer = None
    prediction = None
    get_preds = None
    get_preds_distilled = None
    read_fasta = None
    FastaBatchedDataset = None
    BatchConverter = None

__all__ = [
    "PredictionServer",
    "prediction",
    "get_preds",
    "get_preds_distilled",
    "read_fasta",
    "FastaBatchedDataset",
    "BatchConverter",
]
