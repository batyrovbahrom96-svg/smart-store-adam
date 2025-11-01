"""
data_prep.py
Reads all CSV files in data/raw into pandas DataFrames.
Logs output to project.log.
"""

from pathlib import Path
import pandas as pd
import logging
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
LOG_FILE = PROJECT_ROOT / "project.log"


def setup_logger():
    logger = logging.getLogger("data_prep")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        fh = logging.FileHandler(LOG_FILE)
        fh.setFormatter(fmt)
        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(fmt)
        logger.addHandler(fh)
        logger.addHandler(sh)
    return logger


def read_all_csvs():
    logger = setup_logger()
    if not RAW_DIR.exists():
        logger.error(f"Raw folder not found: {RAW_DIR}")
        return
    for file in RAW_DIR.glob("*.csv"):
        try:
            df = pd.read_csv(file)
            logger.info(f"{file.name} loaded with shape {df.shape}")
        except Exception as e:
            logger.error(f"Error reading {file.name}: {e}")


def main():
    read_all_csvs()


if __name__ == "__main__":
    main()
