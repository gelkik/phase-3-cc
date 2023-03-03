class Review:
    
    def __init__(self, viewer, movie, rating):
        self._viewer = viewer
        self._movie = movie
        self._rating = rating
        # if type(rating) == int:
        #     self._rating = rating
        # else:
        #     raise Exception("Rating must be integer and between 1 and 5.")

        self.add_review_viewer()
        self.add_review_movie()
        self.add_movie_viewer()
        self.add_viewer_movie()

    # rating property goes here!
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self,rating):
        if isinstance(rating,int) and 1 <= len(rating) <=5:
            self._rating = rating
        else:
            raise Exception("Rating must be integer and between 1 and 5.")

    # viewer property goes here!
    @property
    def viewer(self):
        return self._viewer
    
    @viewer.setter
    def viewer(self,viewer):
        from viewer import Viewer
        if isinstance(viewer,Viewer):
            self._viewer = viewer
    
    # movie property goes here!
    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self,movie):
        from movie import Movie
        if isinstance(movie,Movie):
            self._movie = movie
    
    def add_review_viewer(self):
        self._viewer.reviews.append(self)

    def add_review_movie(self):
        self._movie.reviews.append(self)

    def add_movie_viewer(self):
        if self._viewer not in self._movie.viewers:
            self._movie.viewers.append(self._viewer)
        # self._movie.viewers.append(self._viewer)

    def add_viewer_movie(self):
        if self._movie not in self._viewer.movies:
            self._viewer.movies.append(self._movie)
        # self._viewer.movies.append(self._movie)
