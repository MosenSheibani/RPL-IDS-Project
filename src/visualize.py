# src/visualize.py
"""
Visualizes anomalies in RPL control messages and saves results.
Author: [Mohsen Sheibani]
"""

import matplotlib.pyplot as plt
import seaborn as sns
import os

def visualize_and_save(data):
    """
    Creates a scatter plot of anomalies and saves the anomaly report to CSV.
    """
    # Ensure the output directory exists
    os.makedirs('output', exist_ok=True)
    
    # Scatter plot: DIO vs DAO messages with anomalies highlighted
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='dio_messages_per_sec', y='dao_messages_per_sec',
                    hue=data['anomaly'], palette='coolwarm', data=data)
    plt.xlabel('DIO Messages per Second')
    plt.ylabel('DAO Messages per Second')
    plt.title('Anomaly Detection in RPL Control Messages (DIO/DAO/DIS/DDAO)')
    plt.savefig('output/anomaly_plot.png')
    plt.show()

    # Save anomalies to CSV
    anomalies = data[data['anomaly'] == -1]
    anomalies.to_csv('output/rpl_anomalies_report.csv', index=False)
    print(f"Detected {len(anomalies)} anomalies in RPL control messages.")
    print("Anomaly report saved to 'output/rpl_anomalies_report.csv'")