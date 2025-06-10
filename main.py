from ml_process.ml_prepare_ds import prepare_music_dataset
from ml_process.ml_creating_and_training_model import create_and_train_model
from ml_process.ml_test_model import test_music_recommender_model


def main():
    print("Hello from ml-test!")
    prepare_music_dataset()
    create_and_train_model()
    test_music_recommender_model()


if __name__ == "__main__":
    main()
