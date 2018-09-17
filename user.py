class User():

    def __init__(self, user_id = -1, song_id = -1):
        self.user_id = user_id
        self.song_id = set()

    def add_song_id(self, song_id):
        self.song_id.add(song_id)
