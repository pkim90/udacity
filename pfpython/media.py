def jackie(yag, obo):
    first = str(yag)
    second = str(obo)
    print (first)
    print (second)

import webbrowser

class Movie():
    def __init__(self, title, story, poster, trailer):
        self.title = title
        self.story = story
        self.poster = poster
        self.trailer = trailer

    def showTrailer(self):
        webbrowser.open(self.trailer)
