from Heapsort import MaxHeap

settings = ['Fantasy', 'Science Fiction', 'Historical', 'Military', 'Urban', 'Other']
tones = ['Tragic', 'Sad', 'Serious', 'Optimistic', 'Funny']
themes = ['Romance', 'Adventure', 'Coming of Age', 'Slice of Life', 'Social/Political']
eras = ['Silent', 'Black and White', 'Classic', '80s', '1990 - 2005', 'Current']

class Movie:
    def __init__(self, title, setting, tone, theme, era, rating):
        self.title = title
        self.setting = setting
        self.tone = tone
        self.theme = theme
        self.era = era
        self.rating = rating
    def __str__(self):
        return self.title
    

def import_movies():
    movies = []
    with open('Movies.txt','r') as m:
        lines = m.readlines()
    m.close()
    for line in lines:
        movie_lst = line.split(',,')
        movie = Movie(movie_lst[0], movie_lst[1], movie_lst[2], movie_lst[3], movie_lst[4], int(movie_lst[5]))
        movies.append(movie)
    return movies

def add_movies():
    print("Please enter the details of the movie to add")
    movie = []
    movie.append(input("Title: "))
    movie.append(get_lst_entry(settings, 'setting'))
    movie.append(get_lst_entry(tones, 'tone'))
    movie.append(get_lst_entry(themes, 'theme'))
    movie.append(get_lst_entry(eras, 'era'))
    print("Enter a rating from 1 to 10, where 1 is worst and 10 is best:")
    rating = int(input('Rating: '))
    while rating not in range(1, 10):
        print('Invalid Rating - please try again!')
        rating = int(input('Rating: '))
    movie.append(str(rating))
    with open('Movies.txt', 'a') as m:
        m.write('\n' + ',,'.join(movie))

def get_lst_entry(lst, name):
    print(name + " options:")
    for i in range(len(lst)):
        print(str(i+1) + '. ' + lst[i])
    while True:
        user_idx = int(input('Please enter the number corresponding to the movies ' + name + ': '))
        if user_idx in range(1, len(lst) + 1):
            break
        else:
            print("Invalid Selection - please try again")
    return lst[user_idx - 1]

def movie_picker_helper(movies):
    print("What setting should your movie have?")
    setting = get_lst_entry(settings, 'setting')
    print('And what tone would you like?')
    tone = get_lst_entry(tones, 'tone')
    print('And what theme sounds most appealing to you?')
    theme = get_lst_entry(themes, 'theme')
    print('Lastly, please choose an era!')
    era = get_lst_entry(eras, 'era')

    movie_options = MaxHeap()

    for movie in movies:
        if movie.setting == setting and movie.tone == tone and movie.theme == theme and movie.era == era:
            movie_options.add(movie)
    
    return movie_options

#For testing only - remove before finalizing:

#add_movies()
#print(import_movies())