# 1. Dataset: Dictionary mapping movies to sets of genres
movies = {
    'The Matrix': {'Action', 'Sci-Fi'},
    'Inception': {'Action', 'Sci-Fi', 'Thriller'},
    'The Notebook': {'Romance', 'Drama'},
    'Titanic': {'Romance', 'Drama'},
    'Interstellar': {'Sci-Fi', 'Drama'}
}

# 2. Compute Similarity: Intersection over Union (Jaccard Similarity)
def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

# 3. Generate Recommendations
def recommend_by_content(target_movie, num_recommendations=2):
    target_genres = movies[target_movie]
    scores = []
    
    # Calculate similarity score against every other movie
    for movie, genres in movies.items():
        if movie != target_movie:
            score = jaccard_similarity(target_genres, genres)
            scores.append((movie, score))
            
    # Sort by highest score descending
    scores.sort(key=lambda x: x[1], reverse=True)
    
    # Return just the titles of the top N matches
    return [movie for movie, score in scores[:num_recommendations]]

# --- INTERACTIVE USER INPUT ---
print("Available movies: The Matrix, Inception, The Notebook, Titanic, Interstellar")
user_typed_movie = input("Enter a movie you liked: ")

# Check if the movie exists before running the recommendation
if user_typed_movie in movies:
    result = recommend_by_content(user_typed_movie)
    print(f"\nBecause you watched '{user_typed_movie}', we recommend: {result}")
else:
    print(f"\nSorry, '{user_typed_movie}' is not in our database. Please check your spelling and match the exact uppercase/lowercase letters.")