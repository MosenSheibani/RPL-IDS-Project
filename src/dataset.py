# src/dataset.py
"""
Generates a synthetic dataset for RPL control messages (DIO/DAO/DIS/DDAO).
Author: [Mohsen Sheibani]
"""

import pandas as pd
import numpy as np
import os

def create_synthetic_dataset(num_samples=1000):
    """
    Creates a fake dataset for RPL control messages with normal and anomalous behaviors.
    Returns a pandas DataFrame with features: dio, dao, dis, packet loss, and fake DAO-ACK.
    """
    np.random.seed(42)  # For consistent results
    data = {
        'dio_messages_per_sec': np.random.normal(5, 1, num_samples),  # Normal DIO rate
        'dao_messages_per_sec': np.random.normal(2, 0.5, num_samples),  # Normal DAO rate
        'dis_messages_per_sec': np.random.normal(1, 0.3, num_samples),  # Normal DIS rate
        'packet_loss_ratio': np.random.uniform(0.01, 0.1, num_samples),  # Normal packet loss
        'fake_dao_ack_count': np.zeros(num_samples)  # Normal nodes have no fake DAO-ACK
    }

    # Add anomalies (10% of data): DDAO (fake DAO-ACK) and high DIO/DIS rates
    anomaly_indices = np.random.choice(num_samples, size=int(0.1 * num_samples), replace=False)
    for idx in anomaly_indices:
        # Simulate DDAO: high fake DAO-ACK count and increased packet loss
        data['fake_dao_ack_count'][idx] = np.random.randint(1, 5)
        data['packet_loss_ratio'][idx] = np.random.uniform(0.2, 0.5)
        # Simulate DIS Flooding or DAO Inconsistency: high DIO/DIS rates
        if np.random.random() > 0.5:
            data['dio_messages_per_sec'][idx] = np.random.uniform(10, 20)
            data['dis_messages_per_sec'][idx] = np.random.uniform(5, 10)

    df = pd.DataFrame(data)
    
    # Ensure the data directory exists
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/rpl_control_messages.csv', index=False)
    return df