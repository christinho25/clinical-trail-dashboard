import numpy as np
import pandas as pd

SEED = 42
N_PATIENTS = 500
N_SITES = 10

rng = np.random.default_rng(SEED)


def make_sites() -> pd.DataFrame:
    """Create the sites table."""
    ...


def make_patients(sites: pd.DataFrame) -> pd.DataFrame:
    """Create the patients table."""
    ...


if __name__ == "__main__":
    sites = make_sites()
    patients = make_patients(sites)
    print(sites.head())
    print(patients.head())