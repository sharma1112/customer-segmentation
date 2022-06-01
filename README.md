README

Clustering is a technical way of visualizing data points from a large dataset that exhibit similar characteristics or features. Clustering can be used to identify groups/segments of customers in business and can be used to target specific groups and run promotional campaigns to activate a particular segment. 

Although there are other more widely accepted techniques for clustering (like K-Means), Hierarchical Clustering proves to be the best solution to visualize customers of a business according to their spending habits, since the data can be visualized more in an organized hierarchical fashion. 

There are two types of Hierarchical Clustering: Agglomerative (Bottom Up) and Divisive (Top Down). 

In Divisive Clustering, we assign all of the observations to a single cluster and then partition the cluster according to least similar features. Then we proceed recursively until every observation can be fit into at least one cluster. Divisive algorithms are generally more accurate in clustering since they analyze and map every observation to a global model as compared to Agglomerative algorithms. 

In Agglomerative Clustering, we assign each observation to its very own cluster and then compute similarity between each cluster and join clusters showing most similar features. Then we proceed recursively until there is only one cluster at the top. 

Before actually starting to perform clustering on the data, a proximity matrix is to be formed to compute the euclidean distances (distance between each point). The same matrix is then used to update the distance between each cluster.

In the current example, we have a dataset of 200 observations (Source: Kaggle) containing the following headers: Customer ID, Gender, Age, Annual Income (in $) and Spending Score (1–100).

To perform clustering, we need to identify parameters which we'll be using to analyze the data in hand. Columns 3 (Annual Income) and 4 (Spending Score) exhibit good fit for clustering our customers on the basis of their income level and the level of their spending in the store. 

We then identify the optimal number of clusters by visualizing this data in the form of a Dendrogram. The 'ward' linkage method is to be used while making the dendrogram in order to minimize the variance between the clusters.

The optimal number of clusters can be identified by looking at the dendrogram and identifying the number of long branches without horizontal splitting. As we can see from the image above, we can assume 5 as a good number of clusters (3 long clusters within green and 1 each for red and cyan).

Then we proceed to fit the identified clusters in the data and visualize it. Appropriate labels can be given to the clusters post visualization and interpretation of the data.

Source to the original dataset: https://medium.com/r/?url=https%3A%2F%2Fwww.kaggle.com%2Fvjchoudhary7%2Fcustomer-segmentation-tutorial-in-python
