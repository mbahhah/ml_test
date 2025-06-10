import pandas as pd
from sklearn.model_selection import train_test_split
import os

def prepare_music_dataset():
    """
    Prepare the music dataset by importing, processing, and splitting it into training and testing datasets.
    The datasets are then saved to CSV files.
    """    
    # Ensure the datasets directory exists    
    os.makedirs('datasets/testing_ds', exist_ok=True)
    os.makedirs('datasets/testing_ds', exist_ok=True)

    # Step 1: Import dataset
    music_data = pd.read_csv('sample_data/music_ds.csv')

    # Step 2: Prepare dataset
    input = music_data.drop(columns=['genre'])
    output = music_data['genre']

    # Step 3: Split dataset into training & testing datasets
    input_train, input_test, output_train, output_test = train_test_split(input, output, test_size=0.2)

    # Step 4: Save datasets to files
    input_train.to_csv('datasets/training_ds/input_train.csv', index=False)
    input_test.to_csv('datasets/testing_ds/input_test.csv', index=False)
    output_train.to_csv('datasets/training_ds/output_train.csv', index=False)
    output_test.to_csv('datasets/testing_ds/output_test.csv', index=False)
