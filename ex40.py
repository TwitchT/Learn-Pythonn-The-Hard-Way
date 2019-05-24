# We are allowing a new instances
class Song(object):
    # We are defining an attribute inside init
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
# Created a variable that has song lyrics          
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])
                    
bulls_on_parade = Song(["They rally around tha family",
                        "With pokets full of shells"])
# This will print out the songs                        
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()