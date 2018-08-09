# Jupyter Notebooks

* <code>get_ratings.py</code> : This script reads in the raw movie
  list and scrapes Rotten Tomatoes for critics and audience
  scores. Note that there is a substantial amount of manual data
  cleaning of movie titles that don't match between Box Office Mojo
  (the data source for the movie list) and Rotten Tomatoes.

* <code>combine_data.py</code> : A simple helper script that combines
  movie datasets with twitter hashtags and with critics and audience
  scores. Using Pandas.

* <code>RatingsAnalysis.ipynb</code> : Analysis of how critics and
audience scores affect the opening weekend box office gross..


* <code>MoviesOpeningBoxOfficeByMonth-WideRelease.ipynb</code> : Analysis of the impact of release month on the opening weekend box office gross.

* <code>MoviesOpeningBoxOfficeBySeason-WideRelease.ipynb</code> : Analysis of the impact of release season on the opening weekend box office gross.

* <code>movieSentiment-GetTwitterData.ipynb</code> : Code polling the twitter API for tweets related to movies.

* <code>movieSentiment-Plot.ipynb</code> : Analysis and plot of twitter sentiment impact on opening-weekend box office numbers.