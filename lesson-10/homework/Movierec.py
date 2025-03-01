import requests
import random

# TMDB API Key (Replace with your own key)
API_KEY = "4d730257ae821752c1839d55c88357e3"
BASE_URL = "https://api.themoviedb.org/3"

# Get available genres
genre_url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}"
genre_response = requests.get(genre_url).json()
genres = {genre["name"].lower(): genre["id"] for genre in genre_response["genres"]}

# Ask user for a genre
user_genre = input("Enter a movie genre (e.g., Action, Comedy, Drama): ").strip().lower()

if user_genre in genres:
    genre_id = genres[user_genre]
    movie_url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    
    # Fetch movie list
    movie_response = requests.get(movie_url).json()
    movies = movie_response.get("results", [])

    if movies:
        random_movie = random.choice(movies)
        print(f"Recommended {user_genre.capitalize()} Movie: {random_movie['title']}")
        print(f"Overview: {random_movie['overview']}")
    else:
        print("No movies found for this genre.")
else:
    print("Genre not found. Try again.")
