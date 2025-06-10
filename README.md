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
- Python 3.11
- Pandas
- scikit-learn
- joblib

## Installation
To set up the project, you need to create a virtual environment and install the required packages. This can be done using the `uv` tool, which simplifies the process of managing Python environments and dependencies.
```bash
pip install uv
```
Then, you can create a virtual environment and install the dependencies as follows:
```bash
uv init
uv venv .venv -p 3.11
source .venv/bin/activate
uv sync --active
uv pip install -r requirements.txt
```
## Usage
After setting up the environment, you can run the main script to execute the machine learning process:
```bash
uv run main.py
```
## Project Overview
This project demonstrates a simple machine learning workflow using Pandas for data manipulation, scikit-learn for building and evaluating a machine learning model, and joblib for saving the trained model. The main steps include:
1. **Data Preparation**: Loading and preparing the dataset using Pandas.
2. **Model Training**: Creating and training a machine learning model using scikit-learn.
3. **Model Testing**: Evaluating the model's performance on a test dataset.
4. **Model Serialization**: Saving the trained model to a file using joblib for future use.
## Dependencies
The project requires the following Python packages, which are listed in `requirements.txt`:
```plaintext
pandas
scikit-learn
joblib
```
## Project Files
- `main.py`: The main script that orchestrates the machine learning process.
- `requirements.txt`: A file listing the required Python packages.
- `sample_data/music_ds.csv`: A sample dataset used for training and testing the model.
- `datasets/testing_ds/input_test.csv`: Input data for testing the model.
- `datasets/testing_ds/output_test.csv`: Expected output for testing the model.
- `datasets/training_ds/input_train.csv`: Input data for training the model.
- `datasets/training_ds/output_train.csv`: Expected output for training the model.
- `ml_process/ml_creating_and_training_model.py`: Script for creating and training the machine learning model.
- `ml_process/ml_prepare_ds.py`: Script for preparing the dataset.
- `ml_process/ml_test_model.py`: Script for testing the trained model.
- `models/music_recommender_model.pkl`: The serialized machine learning model.  
- `.gitignore`: A file specifying files and directories to be ignored by Git.
- `.python-version`: Specifies the Python version for the project.

## Note
if you don't have uv installed, you can install it using pip:
```bash
pip install uv
```
## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
Contributions are welcome! If you have suggestions for improvements or find bugs, please open an issue or submit a pull request.
