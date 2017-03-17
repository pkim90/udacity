def jackie(yag, obo):
    first = str(yag)
    second = str(obo)
    print (first)
    print (second)

import webbrowser

class Movie():
    """This class is useful for storing information for movies, or any other thing you can think of."""
    VALID_RATINGS = ['P', 'PG', 'PG-13', 'R']
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
 
