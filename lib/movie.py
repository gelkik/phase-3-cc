class Movie:
    all = []
    def __init__(self, title):
        # if type(title) == str:
        #     self._title = title
        # else:
        #     raise Exception("Title must be string.")
        if type(title) == str and len(title) > 0:
            self._title = title
        else:
            raise Exception('Movie title must be string.')
        self.reviews = []
        self.viewers = []
        self.reviewers = []    
        Movie.all.append(self)

    # title property goes here!
    @property
    def title(self):
        return self._title
    
    # @title.setter
    # def title(self,title):
    #     if type(title) == str and len(title) > 0:
    #         self._title = title
    #     else:
    #         raise Exception('Movie title must be string.')

    def average_rating(self):
        sum = 0
        for num in self.reviews:
            sum += num
        avg = sum/len(self.reviews)
        return avg

    @classmethod
    def highest_rated(cls):
        li = []
        for num in cls.all.reviews:
            li.append(num.average_rating())
        max = max(li)
        


# Movie.all = []
# movie_1 = Movie(title="Avatar: The Way of Water")
# movie_1.reviews = [1, 1, 1, 2, 3, 4, 4, 5]
# movie_2 = Movie(title="Scarface")
# movie_2.reviews = [1, 1, 1, 1, 1, 1]
# movie_3 = Movie(title="Rashomon")
# movie_3.reviews = [5, 5, 5, 5, 5, 5, 5]
# movie_4 = Movie(title="My Neighbor Totoro")
# movie_4.reviews = [4, 3, 4, 3, 2, 5, 4]
# assert Movie.highest_rated().title == "Rashomon"