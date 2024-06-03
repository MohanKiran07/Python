import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

# Sample data
movies = pd.DataFrame({
    'movieid': [1, 2, 3, 4, 5],
    'moviename': ['movie1', 'movie2', 'movie3', 'movie4', 'movie5']
})

ratings = pd.DataFrame({
    'userid': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],
    'movieid': [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 1, 1, 3, 5],
    'rating': [5, 6, 7, 7, 8, 5, 6, 8, 5, 7, 6, 6, 5, 7, 6]
})

# Analysis
def recommendation(userid):
    # Compute average ratings
    avgratings = ratings.groupby('movieid')['rating'].mean().reset_index()
    avgratings.rename(columns={'rating': 'avgrating'}, inplace=True)
    
    # Merge movies with their average ratings
    recommendations = movies.merge(avgratings, on='movieid')
    
    # Plot
    bars=plt.bar(recommendations['moviename'], recommendations['avgrating'], color='k')
    for bar in bars:
        yval=bar.get_height()
        plt.text(bar.get_x()+bar.get_width()/2,yval+0.1,round(yval,2),ha='center',va='bottom',c='b')
    
    plt.xlabel('Movie Name',c='r')
    plt.ylabel('Average Ratings',c='r')
    plt.title('Average Movie Ratings Recommendation System',c='b')
    plt.show()

# Example usage
recommendation(1)