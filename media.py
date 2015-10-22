import webbrowser

# The Movie Class store info of the movie, 'director' is Class Director object, 'main_actor' is Class Director object
class Movie():
	"""Store Movie Info"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, director, main_actor):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.director = director
		self.main_actor = main_actor

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)