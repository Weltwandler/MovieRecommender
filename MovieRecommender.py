from Movies import import_movies, add_movies, Movie
from DoublyLL import DoublyLinkedList

def pick_movies():
    pass

def get_choice():
    print('To add movies to your list, press 1.')
    print('To get a movie recommendation, press 2.')
    choice = input()
    if choice not in ['1', '2']:
        print('Invalid Selection - please try again!')
        choice = get_choice()
    return choice

movies = import_movies()

print('Welcome to Movie Recommender!')
choice = get_choice()
if choice == '1':
    add_movies()
else:
    pick_movies()
