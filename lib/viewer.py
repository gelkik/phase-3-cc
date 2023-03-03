class Viewer:
    all = []
    
    def __init__(self, username):
        if type(username) == str and 6 <= len(username) <= 16 and username not in Viewer.all:
            self._username = username
            Viewer.all.append(username)
        else:
            raise Exception('Username must be string and between 6 and 16 characters.')
        self.reviews = []
        self.movies = []
        self.reviewed_movies = []
        for num in self.movies:    
            self.reviewed_movies.append(num.title)

    # username property goes here!
    @property
    def username(self):
        return self._username
    
    # @username.setter
    # def username(self,username):
    #     if type(username) == str and 6 <= len(username) <= 16:
    #         self._username = username
    #     else:
    #         raise Exception('Username must be string and between 6 and 16 characters.')

    def reviewed_movie(self, movie):
        if movie in self.reviewed_movies:
            return True
        else:
            return False

    def rate_movie(self, movie, rating):
        from review import Review
        if movie in self._reviews:
            self.reviews.rating = rating
        else:
            Review(self,movie,rating)

# viewer = Viewer(username="luckier_the_cat")
# movie = Movie("The Bourne Identity")
# viewer.rate_movie(movie, 3)
# assert movie in viewer.reviewed_movies
# assert viewer.reviews[0].rating == 3
# viewer.rate_movie(movie, 4)
# assert len(viewer.reviewed_movies) == 1
# assert viewer.reviews[0]