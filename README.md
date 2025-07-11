# Movie Recommender System

This project is a Movie Recommender System built using Streamlit. It provides movie recommendations based on similarity metrics and displays movie posters fetched from external APIs.

## Features

- Two versions of the app:
  - `app.py`: Uses The Movie Database (TMDB) API to fetch movie posters.
  - `app1.py`: Uses the OMDb API to fetch movie posters (requires an API key).

- Interactive UI to select a movie and get top 5 recommended movies with posters.

## Setup Instructions

1. Clone the repository and navigate to the project directory.

2. (Optional but recommended) Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. For `app1.py` (OMDb API version), create a `.env` file in the project root with your OMDb API key:

```
OMDB_API_KEY=your_api_key_here
```

You can get a free API key from [OMDb API](http://www.omdbapi.com/apikey.aspx).

## Running the App

To run the TMDB API version:

```bash
streamlit run app.py
```

To run the OMDb API version:

```bash
streamlit run app1.py
```

## Data Files

- `movie_list.pkl`: Pickle file containing the list of movies.
- `similarity.pkl`: Pickle file containing the similarity matrix used for recommendations.

Make sure these files are present in the project directory.

## Notes

- The TMDB API key is hardcoded in `app.py`. You may want to replace it with your own key for production use.
- The OMDb API key must be set in the `.env` file for `app1.py` to work correctly.

## License

This project is open source and free to use.
