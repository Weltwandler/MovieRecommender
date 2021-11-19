from Movies import import_movies, add_movies, movie_picker_helper, Movie
from DoublyLL import DoublyLinkedList
from Heapsort import MaxHeap

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
    movie_options = movie_picker_helper(movies)
    movie_list = DoublyLinkedList()
    while len(movie_options.heap_list) > 1:
        print(len(movie_options.heap_list))
        movie_list.add_to_tail(movie_options.retrieve_max())
    movie_to_show = movie_list.head_node
    if movie_to_show != None:
        print("Your recommended movie is: " + str(movie_to_show.get_value()))
        choice = int(input("Press 2 to get the next-best recommendation or 0 to exit: "))
        movie_to_show = movie_to_show.get_next_node()
    else:
        choice = 0
    while choice > 0:
        if movie_to_show:
            print("Your recommended movie is: " + str(movie_to_show.get_value()))
            choice = int(input("Press 1 to go back, 2 to get the next-best recommendation or 0 to exit: "))
            if choice == 1:
                movie_to_show = movie_to_show.get_prev_node()
            elif choice == 2:
                movie_to_show = movie_to_show.get_next_node()
        else:
            print("There are no more recommendations.")
            choice = int(input("Press 1 to go back or 0 to exit: "))
            movie_to_show = movie_list.tail_node
    print("Have a nice day!")
