#Import all required packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

#Import and read the dataset
ds=pd.read_csv('Mall_Customers.csv')
#Show the data headers
ds.head()

#Creating the feature matrix, X
X=ds.iloc[:,[3,4]].values

#Creating a Dendrogram to identify optimal number of clusters
import scipy.cluster.hierarchy as sch
#Using Ward method to minimize variance within the clusters
dendrogram=sch.dendrogram(sch.linkage(X, method = 'ward'))
#Plotting the Dendrogram
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.show()

#Fitting the identified clusters to data
from sklearn.cluster import AgglomerativeClustering
hc=AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
y_hc=hc.fit_predict(X)

#Visualizing the Cluster
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 100, c='red', label = 'High Income, Low Spenders')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c='blue', label = 'Average Spenders')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c='green', label = 'High Income, High Spenders')
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s = 100, c='cyan', label = 'Low Income, High Spenders')
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s = 100, c='magenta', label = 'Low Income, Low Spenders')

#Plotting the visualization
plt.title('Customer Clusters')
plt.xlabel('Annual Income ($)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
