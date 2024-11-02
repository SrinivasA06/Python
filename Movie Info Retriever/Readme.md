## Movie Information Retrieval System

This project is a movie information retrieval system that allows users to search for movies by name and retrieves relevant details using the TMDB API. 
It classifies movies based on ratings and provides an interactive GUI for easy user interaction.

## Data

The data used in this project comes from two main sources:

1. **TMDB (The Movie Database) API**:
   - The TMDB API provides access to a large dataset of movies, including titles, ratings, genres, release dates, and much more. This project uses the API to fetch real-time movie data based on user queries.
   - **Data Format**: The API returns data in JSON format, which is parsed to extract relevant information such as title, genre, and rating.

2. **Local CSV Data (`tmdb_5000_movies.csv`)**:
   - A local CSV file, `tmdb_5000_movies.csv`, serves as an additional dataset. It contains preloaded movie data, which may include information not dynamically retrieved from the API.
   - **Fields**: Key fields in this dataset include `id`, `title`, `genres`, `vote_average`, and `popularity`.

### API Integration

To use the TMDB API in this project:

1. **Obtain an API Key**:
   - Sign up for a free API key from [The Movie Database](https://www.themoviedb.org/documentation/api).
   - Once you have the key, add it to your environment or directly in the code where specified.

2. **API Endpoints**:
   - This project primarily uses the `/search/movie` endpoint to retrieve movie details based on the name provided by the user.
   - Additional endpoints can be integrated for more detailed information, such as actor details or movie recommendations.

3. **Data Processing**:
   - After retrieval, movie details are processed and classified based on their ratings to categorize movies as "Good", "Bad", or "Average".
   - This classification enriches the data, helping users make quick assessments about movies.

### Example API Response Structure

A sample API response from the TMDB API might look like:

```json
{
  "page": 1,
  "results": [
    {
      "id": 12345,
      "title": "Sample Movie",
      "overview": "This is a sample overview of the movie.",
      "vote_average": 7.5,
      "genre_ids": [18, 28]
    }
  ]
}
```
## Usage
- Obtain a TMDB API key and add it to your environment or directly in the code where specified.
- Run the program (Final.ipynb), which includes a GUI for movie searching.
- Enter a movie name to retrieve and display details including title, rating, genre, and classification as "Good", "Bad", or "Average."

## Features
- Search Query Processing: Accepts user queries for movie names and processes them for API retrieval.
- Data Retrieval: Fetches data from the TMDB API, including movie titles, ratings, genres, etc.
- Classification: Classifies movies based on ratings relative to genre averages.
- User Interaction: Provides an interactive GUI for user-friendly search and information display.
