from pathlib import Path

import pandas as pd
import streamlit as st


DATA_DIR = Path(__file__).resolve().parents[2] / "data"


@st.cache_data
def load_data():
    datasets = {}

    for csv_file in DATA_DIR.glob("*.csv"):
        datasets[csv_file.stem] = pd.read_csv(csv_file)

    return datasets