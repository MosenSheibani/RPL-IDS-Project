# src/anomaly_detection.py
"""
Detects anomalies in RPL control messages using Isolation Forest.
Author: [Mohsen Sheibani]
"""

from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(data):
    """
    Detects anomalies in RPL control messages using Isolation Forest.
    Returns the DataFrame with an 'anomaly' column (-1 for anomalies, 1 for normal).
    """
    features = ['dio_messages_per_sec', 'dao_messages_per_sec', 'dis_messages_per_sec',
                'packet_loss_ratio', 'fake_dao_ack_count']
    X = data[features]

    # Train Isolation Forest model
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(X)

    # Predict anomalies
    data['anomaly'] = model.predict(X)
    return data