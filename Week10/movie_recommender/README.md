# What should we watch tonight?  A Movie Recommender System

For this project, I built a movie recommender based on the idea that people with similar tastes as ours may also like similar movies.  This is known as a collaborative filtering based approach to recommendation.  The data source I used to build my recommender is the MovieLens 20 Million Dataset, which consist of 20 million ratings of movies.  To run the code in these notebooks, you will need to download this [data set](https://grouplens.org/datasets/movielens/20m/).

**Repository Structure**

* python/notebooks: This folder consists of a few different ipython Notebooks that I implemented for this project.  Some of these notebooks were for my own exploration purposes, so these will be less helpful and/or confusing for somebody wanting to reproduce my recommender system.  The main notebooks I would like to point out are:
    - Movie_Recommender_matrix_factorization.ipynb: In this notebook, I implemented Nick Becker's matrix factorization method discussed in his [blog post](https://beckernick.github.io/matrix-factorization-recommender/).
    - Movie_Recommender_model_optimization.ipynb: This notebook is an extension of what I previously did in the Movie_Recommender_matrix_factorization.ipynb notebook. However, my goal in this notebook was to try and optimize my recommendation model.
* docs/presentations:
    - BSturm_movie_recommender_180627_update1.pdf: Slide deck providing an overview of the project.
* docs/mvp:
    - BSturm_movie_recommender_MVP_180607.pdf: Contains the document describing my minimum viable product.
* docs/summary:
    - BSturm_movie_recommender_summary_180627.pdf: Contains a brief summary document describing the goals of my project, the methods used, and things I'd do differently next time.
