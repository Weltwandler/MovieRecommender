def import_movies():
    movies = []
    with open('Movies.txt','r') as m:
        lines = m.readlines()
    m.close()
    for line in lines:
        movie_lst = line.split(',,')
        movie = {}
        movie['title'] = movie_lst[0]
        movie['genre'] = movie_lst[1]
        movie['tone'] = movie_lst[2]
        movie['theme'] = movie_lst[3]
        movie['era'] = movie_lst[4]
        movie['rating'] = int(movie_lst[5])
        movies.append(movie)
    return movies
