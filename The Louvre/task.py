class Painting:
    museum = 'Louvre'

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def get_info(self):
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the {self.museum}.')
inp_title = input()
inp_artist = input()
inp_year = input()

s = Painting(inp_title, inp_artist, inp_year)
s.get_info()

"""
class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        self.info = f'"{self.title}" by {self.artist} ({self.year}) hangs in the {Painting.museum}.'


inp_title = input()
inp_artist = input()
inp_year = input()

s = Painting(inp_title, inp_artist, inp_year)
print(s.info)
"""