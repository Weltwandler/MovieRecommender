from Movies import import_movies, add_movies, movie_picker
from DoublyLL import DoublyLinkedList

# Helper method:

def get_choice():
    print('To add movies to your list, press 1.')
    print('To get a movie recommendation, press 2.')
    choice = input()
    if choice not in ['1', '2']:
        print('Invalid Selection - please try again!')
        choice = get_choice()
    return choice

# Main program starts here:

movies = import_movies()

print('Welcome to Movie Recommender!')
# Choose whether to add a movie to the list or to get a movie recommendation
choice = get_choice()
if choice == '1':
    add_movies()
else:
    # Generate the max-heap of movies that fit the requirements
    movie_options = movie_picker(movies)
    # Generate the doubly-linked list
    movie_list = DoublyLinkedList()
    while len(movie_options.heap_list) > 1:
        movie_list.add_to_tail(movie_options.retrieve_max())
    # Present the first recommendation to the user
    movie_to_show = movie_list.head_node
    if movie_to_show != None:
        print("Your recommended movie is: " + str(movie_to_show.get_value()))
        choice = int(input("Press 2 to get the next-best recommendation or 0 to exit: "))
        # Move to the next movie in the list - note this happens before the loop that checks if the user wants another movie in order to make the navigation work
        movie_to_show = movie_to_show.get_next_node()
    else:
        # End program if there are no matching movies
        print("No movies match your choices :-(")
        choice = 0
    # Present additional options to the user if they ask for them
    while choice > 0:
        if movie_to_show:
            print("Your recommended movie is: " + str(movie_to_show.get_value()))
            # Navigate backwards or forwards through the list
            choice = int(input("Press 1 to go back, 2 to get the next-best recommendation or 0 to exit: "))
            if choice == 1:
                movie_to_show = movie_to_show.get_prev_node()
            elif choice == 2:
                movie_to_show = movie_to_show.get_next_node()
        else:
            # End of the list has been reached
            print("There are no more recommendations.")
            choice = int(input("Press 1 to go back or 0 to exit: "))
            # The following line refers to the tail node rather than using get_prev_node since movie_to_show is "None" at this stage
            movie_to_show = movie_list.tail_node
    # Program ends here
    print("Have a nice day!")
