import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

def create_and_train_model():
    """
    Create and train a machine learning model for music recommendation.
    The model is trained on the training dataset and saved to a file.
    """
    # Step 1: Load datasets from files
    input_train = pd.read_csv('datasets/training_ds/input_train.csv')
    output_train = pd.read_csv('datasets/training_ds/output_train.csv')

    # Step 2: Select a machine learning model
    model = DecisionTreeClassifier()

    # Step 3: Train the selected model
    model.fit(input_train, output_train)

    # Step 4: Save the trained model to a file
    joblib.dump(model, 'models/music_recommender_model.pkl')
