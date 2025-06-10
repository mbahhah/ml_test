import pandas as pd
from sklearn.metrics import accuracy_score
import joblib

def test_music_recommender_model():
    """
    Test the music recommender model by importing the test dataset, loading the trained model,
    making predictions, and measuring the accuracy of the model.
    """
    # Step 1: Import dataset
    input_test = pd.read_csv('datasets/testing_ds/input_test.csv')
    output_test = pd.read_csv('datasets/testing_ds/output_test.csv')

    # Step 2: Import model
    model = joblib.load('models/music_recommender_model.pkl')

    # Step 3: Testing model
    predictions = model.predict(input_test)

    # Step 4: Measure accuracy to make required improvements if needed
    score = accuracy_score(output_test, predictions)
    print(f"Model Accuracy: {score}")
