import numpy as np
import pandas as pd
import logging

class DataProcessing:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def normalize_data(self, data):
        """
        Normalize the input data to a range of [0, 1].
        :param data: A numpy array of numerical data.
        :return: A normalized numpy array.
        """
        if not isinstance(data, np.ndarray):
            logging.error("Input data must be a numpy array.")
            return None
        min_val = np.min(data)
        max_val = np.max(data)
        normalized_data = (data - min_val) / (max_val - min_val)
        logging.info("Data normalized successfully.")
        return normalized_data

    def filter_data(self, data, threshold):
        """
        Filter the input data based on a threshold.
        :param data: A numpy array of numerical data.
        :param threshold: A threshold value for filtering.
        :return: A numpy array of filtered data.
        """
        if not isinstance(data, np.ndarray):
            logging.error("Input data must be a numpy array.")
            return None
        filtered_data = data[data > threshold]
        logging.info(f"Data filtered with threshold {threshold}.")
        return filtered_data

    def load_csv(self, file_path):
        """
        Load data from a CSV file into a pandas DataFrame.
        :param file_path: Path to the CSV file.
        :return: A pandas DataFrame containing the data.
        """
        try:
            data = pd.read_csv(file_path)
            logging.info(f"Data loaded from {file_path}.")
            return data
        except Exception as e:
            logging.error(f"Failed to load data from {file_path}: {e}")
            return None

# Example usage
if __name__ == "__main__":
    dp = DataProcessing()
    sample_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    normalized = dp.normalize_data(sample_data)
    logging.info(f"Normalized Data: {normalized}")

    filtered = dp.filter_data(sample_data, 5)
    logging.info(f"Filtered Data: {filtered}")

    # Load a CSV file (ensure you have a valid CSV file path)
    # df = dp.load_csv("path/to/your/data.csv")
    # logging.info(f"DataFrame: {df}")
