
class Music_Library():

    def __init__(self):
        self.library = []

    def add_track(self, track):
        self.library.append(track)

    def track_list(self):
        return self.library