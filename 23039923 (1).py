# -*- coding: utf-8 -*-
"""23039923.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SHHA2MRUN2Ndc19XNLCRn3sohyRWh5K-
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, confusion_matrix
from yellowbrick.cluster import KElbowVisualizer

def load_mushroom_dataset():
    """
    Function to load the Mushroom dataset from UCI repository.
    Returns:
    - mushroom_df: DataFrame containing the Mushroom dataset.
    """
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
    columns = ["class", "cap_shape", "cap_surface", "cap_color", "bruises", "odor", "gill_attachment",
               "gill_spacing", "gill_size", "gill_color", "stalk_shape", "stalk_root", "stalk_surface_above_ring",
               "stalk_surface_below_ring", "stalk_color_above_ring", "stalk_color_below_ring", "veil_type",
               "veil_color", "ring_number", "ring_type", "spore_print_color", "population", "habitat"]
    return pd.read_csv(url, header=None, names=columns)

def preprocess_data(df):
    """
    Function to preprocess the Mushroom dataset.
    Args:
    - df: DataFrame containing the Mushroom dataset.
    Returns:
    - df: Preprocessed DataFrame.
    """
    label_encoders = {}
    for column in df.columns:
        label_encoders[column] = LabelEncoder()
        df[column] = label_encoders[column].fit_transform(df[column])
    return df

def perform_clustering(df):
    """
    Function to perform clustering using k-means.
    Args:
    - df: DataFrame containing the preprocessed Mushroom dataset.
    Returns:
    - cluster_labels: Labels assigned to each data point by k-means clustering.
    """
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    return kmeans.fit_predict(df)

def visualize_relational_graph(df, cluster_labels):
    """
    Function to visualize the clusters using a scatter plot.
    Args:
    - df: DataFrame containing the preprocessed Mushroom dataset.
    - cluster_labels: Labels assigned to each data point by k-means clustering.
    """
    pca = PCA(n_components=2)
    mushroom_pca = pca.fit_transform(df)

    plt.figure(figsize=(10, 6))
    plt.scatter(mushroom_pca[:, 0], mushroom_pca[:, 1], c=cluster_labels, cmap='viridis', s=50, alpha=0.5)
    plt.title('K-means Clustering of Mushroom Dataset')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.colorbar(label='Cluster')
    plt.show()

def visualize_categorical_graph(df):
    """
    Function to visualize the distribution of mushroom classes using a histogram.
    Args:
    - df: DataFrame containing the preprocessed Mushroom dataset.
    """
    plt.figure(figsize=(8, 6))
    df['class'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
    plt.title('Distribution of Mushroom Classes')
    plt.xlabel('Class')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()

def visualize_statistical_graph(df, cluster_labels):
    """
    Function to visualize the confusion matrix.
    Args:
    - df: DataFrame containing the preprocessed Mushroom dataset.
    - cluster_labels: Labels assigned to each data point by k-means clustering.
    """
    plt.figure(figsize=(8, 6))
    cm = confusion_matrix(df['class'], cluster_labels)
    plt.imshow(cm, cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.colorbar()
    plt.xticks([0, 1], ['Predicted Poisonous', 'Predicted Edible'])
    plt.yticks([0, 1], ['True Poisonous', 'True Edible'])
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    for i in range(2):
        for j in range(2):
            plt.text(j, i, format(cm[i, j], 'd'), ha="center", va="center", color="white" if cm[i, j] > cm.max() / 2 else "black")
    plt.show()

def visualize_elbow_plot(df):
    """
    Function to visualize the elbow plot to find the optimal number of clusters.
    Args:
    - df: DataFrame containing the preprocessed Mushroom dataset.
    """
    model = KMeans(n_init=10)
    visualizer = KElbowVisualizer(model, k=(1, 11))
    visualizer.fit(df)
    visualizer.show()



def main():
    # Load dataset
    mushroom_df = load_mushroom_dataset()

    # Preprocess data
    mushroom_df = preprocess_data(mushroom_df)

    # Perform clustering
    cluster_labels = perform_clustering(mushroom_df)

    # Visualize graphs
    visualize_relational_graph(mushroom_df, cluster_labels)
    visualize_categorical_graph(mushroom_df)
    visualize_statistical_graph(mushroom_df, cluster_labels)
    visualize_elbow_plot(mushroom_df)

if __name__ == "__main__":
    main()

