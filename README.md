# Simple Machine Learning Sample Project using Pandas, scikit-learn, and joblib libraries

This project is a simple demonstration of using Pandas for data manipulation, scikit-learn for machine learning, and joblib for model serialization. It is designed to be run in a virtual environment created with uv.
## Project Structure
```
.
├── main.py
├── requirements.txt
├── sample_data
│   └── music_ds.csv
├── datasets
│   └── testing_ds
│       └── input_test.csv
│       └── output_test.csv
├── └── training_ds
│       └── input_train.csv
│       └── output_train.csv
├── ml_process
│   ├── ml_creating_and_training_model.py
│   ├── ml_prepare_ds.py
│   └── ml_test_model.py
├── models
│   └── music_recommender_model.pkl
├── .gitignore
├── .python-version
├── .requirements.txt
├── .uv.lock
└── README.md
```
## Requirements
## How to Run
uv init
uv venv .venv -p 3.11
source .venv/bin/activate
uv sync --active
uv pip install -r requirements.txt
uv run main.py

## Note
if you don't have uv installed, you can install it using pip:
```bash
pip install uv
```