class Player:
    def __init__(self, name, video_link, duration):
        self.name = name
        self.video_link = video_link
        self.duration = duration
        self.last_time = 0
        self.quality = 'HD'

    def play(self, video_address):
        if video_address:
            print(f"Playing {self.name}")
            return True
        else:
            print(f"Video not found: {self.name}")
            return False

    def pause(self):
        print("Pausing...")

    def save_last_time(self, last_time):
        self.last_time = last_time
        print(f"Last time saved: {self.last_time}")

    def change_quality(self, new_quality):
        self.quality = new_quality
        print(f"Quality changed to {self.quality}")

import os

class Film:
    def __init__(self, title, description, director, writer, cast, running_time, country,
                 language, imdb_rating, year, budget, box_office, profitable, oscar_nominated,
                 oscar_win, trailer):
        self.title = title
        self.storage_address = os.path.join('film_storage', title[0].upper(), f'{title}.txt')
        self.upload_file()
        self.trailer = trailer

    def upload_file(self):
        with open(self.storage_address, 'w') as file:
            file.write(f'Title:\n  {self.title}\n\nDescription:\n  {self.description}\n\nDirector:\n  {self.director}\n'
                       f'  {self.co_director}\n\nWriter:\n  {self.writer}\n\nCast(actors):\n  {", ".join(self.cast)}\n\n'
                       f'Running time:\n  {self.running_time} minutes\n\nCountry:\n  {self.country}\n\nLanguage:\n  {self.language}\n\n'
                       f'IMDb RATING:\n  {self.imdb_rating}\n\nYear:\n  {self.year}\n\nBudget:\n  {self.budget}\n\n'
                       f'Box office:\n  {self.box_office}\n\nProfitable:\n  {self.profitable}\n\nOscar nominated:\n  {self.oscar_nominated}\n\n'
                       f'Oscar win:\n  {self.oscar_win}\n\nTrailer:\n  {self.trailer}\n')

    def get_film_address(self):
        return self.storage_address
