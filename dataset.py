from sklearn.model_selection import train_test_split
import pandas as pd
import os

def extract_data():

    append_mode = os.path.isfile("data/train.csv")

    df = pd.read_csv('data/churn_data_collection.csv')

    train_size = 0.8  # 80% for training and 20% for testing

    train_data, test_data = train_test_split(df, train_size=train_size, random_state=42)
        
    train_data.to_csv("data/train.csv", mode="a", header=not append_mode, index=False)
    test_data.to_csv("data/test.csv", mode="a", header=not append_mode, index=False)

    print("Extracted data from source successfully")

if __name__ == "__main__":
    extract_data()