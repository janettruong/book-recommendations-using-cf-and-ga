# book recommender using cf and ga
 A Recommender System using Collaborative Filtering and Genetic Algorithm. We implemented a paper with a novel approach in building a robust recommender system named BLIGA to solve problems commonly seen in such systems, such as cold-start and sparsity.
 
 The BLIGA consists of 3 filtering levels:
 1. Semantic similarity. This is the level of similarity between features of items in a recommended list.
 2. Total predicted score. This is the fitness value of each recommended list, calculated by using the similarity between users and the AU (active user).

We modified the original BLIGA and tuned the hyperparameters. We also made some experiments to test the performance of the system.

Then we implemented a hyperparameter combination with top performance in a UI. The UI design is based on that of [UEH Smart Digital Library][https://smartlib.ueh.edu.vn/], a key service of UEH University in Vietnam.

We have reported our process of designing, implementing, and testing in our final report.

# Guidelines
[Our final Report](UEH500Report.pdf)
[BLIGA system](Algorithm/main.py)
[The UI for BLIGA](UI/main.py)
[Statistical Analysis of datasets](Algorithm/statistics.ipynb)
