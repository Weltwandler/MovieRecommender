# Movie Recommender - Project Overview

## What it is
Movie Recommender is a Python application designed to recommend movies based on what the user feels like watching.

## How it works

The user answers four questions about their preferences - namely Genre, Tone, Theme and Era - and is then provided with up to three movies that best fit those stated preferences

**Genre** in this context refers to the setting of the movie. It can be Fantasy, Science Fiction, Historical, Military, Urban or Other.

**Tone** can be Tragic, Sad, Serious, Optimistic or Funny.

**Theme** refers to plot archetypes - it can be Romance, Adventure, Coming of Age, Slice of Life or Social/Political

**Era** refers to the era the movie was made in and can be Silent, Black and White, Classic, 80s, 1990-2005 or Current

Each movie will also have a rating, and the recommendation will be for the highest-rated movies that fit the criteria.

There will also be a part of the application that allows for adding new movies to the list.

## How it is Structured

The application contains several separate Python files - the main MovieRecommender.py, a file with movie data called Movies.py, as well as a number of separate files including the classes for the custom data structures and the MovieAdder.py file.

## To Do:

* Design Data structure(s)
* Create sample movies list
* Write main program