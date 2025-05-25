# main.py
"""
Main script for RPL Intrusion Detection System (IDS).
Detects DDAO and other RPL control message attacks (DIO/DAO/DIS).
Author: [Mohsen Sheibani]
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.dataset import create_synthetic_dataset
from src.anomaly_detection import detect_anomalies
from src.visualize import visualize_and_save

def main():
    print("Starting RPL IDS...")
    # Create synthetic dataset
    data = create_synthetic_dataset(num_samples=1000)
    print("Synthetic dataset created with 1000 samples.")
    print("Sample data preview:\n", data.head())  # Check data

    # Detect anomalies
    data = detect_anomalies(data)
    print("Anomaly detection completed.")
    print("Anomaly counts:", data['anomaly'].value_counts())  # Check anomaly distribution

    # Visualize and save results
    visualize_and_save(data)
    print("IDS process finished.")

if __name__ == "__main__":
    main()