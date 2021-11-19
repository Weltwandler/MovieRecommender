# Movie Recommender - Project Overview

## What it is
Movie Recommender is a Python application designed to recommend movies based on what the user feels like watching.

## How it works

The user answers four questions about their preferences - namely Genre, Tone, Theme and Era - and is then provided with a movie recommendation that best fits those stated preferences, and can ask for more movies to be shown if they don't like the first option.

**Setting** The setting of the movie. It can be Fantasy, Science Fiction, Historical, Military, Urban or Other.

**Tone** can be Tragic, Sad, Serious, Optimistic or Funny.

**Theme** refers to plot archetypes - it can be Romance, Adventure, Coming of Age, Slice of Life or Social/Political

**Era** refers to the era the movie was made in and can be Silent, Black and White, Classic, 80s, 1990-2005 or Current

Each movie will also have a rating, and the recommendation will be for the highest-rated movie that fits the criteria.

There will also be a part of the application that allows for adding new movies to the list.

## How it is Structured

The application contains several separate Python files - the main MovieRecommender.py, a file with movie data-specific methods called Movies.py, as well as a number of separate files including the classes for the custom data structures. The movie data itself will be stored in a txt file, which is imported and stored in a list at the start of running the application.

When the user has chosen their preferences, the list is traversed and every movie that matches is added to a new max-heap, from which the highest rated movie is then retrieved via a heapsort algorithm. This movie is then stored in a Doubly linked list, to which any additional movies the user requests are also added, so the user can traverse the list if they want to return to a previous movie.

## Future enhancements

One relatively simple enhancement that would improve the overall experience would be for users to be able to ignore certain categories - for example, if the user does not care about the setting, but does care about the other categories. If the user chooses to ignore all settings, they simply get the highest-rated movies overall. This would require refactoring the get_lst_entry method, the add_movie method and the movie_picker method so that there is an additional valid selection option in movie_picker as opposed to add_movie.

A more complex change would be to replace the categories withs a "tag" or "label" style system. This would actually be less useful for a "what movie do you want to watch right now" tool, but would allow a setup where users can enter a few movies they like and the system will then find movies that are similar. This would essentially create a functionality similar to many streaming or online shopping portals, and could also be linked to a users viewing history.

Finally, in a real-world setting, the application should use a proper database rather than a simple text file.