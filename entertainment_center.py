import fresh_tomatoes
import media
import media_person

# Create Movie objects, Director objects, Actor objects and open the page.
# The page doesn't work very well in Safari

christopher_nolan = media_person.Director("Christopher Nolan", "male", 
										  "avatar/Christopher_Nolan.jpg")
matthew_mcConaughey = media_person.Actor("Matthew McConaughey", "male", 
										 "avatar/Matthew_McConaughey.jpg")
interstellar = media.Movie(
	"Interstaller",
	"A team of explorers travel through a wormhole in space in an attempt to \
	ensure humanity's survival.",
	"https://upload.wikimedia.org/wikipedia/zh/b/bc/Interstellar_film_poster.jpg",
	"https://www.youtube.com/watch?v=0vxOhd4qlnA",
	christopher_nolan,
	matthew_mcConaughey)

christian_bale = media_person.Actor("Christian Bale", "male", 
									"avatar/Christian_Bale.jpg")
the_dark_king = media.Movie(
	"Batman: The Dark Knight",
	"When the menace known as the Joker wreaks havoc and chaos on the \
	people of Gotham, the caped crusader must come to terms with one of \
	the greatest psychological tests of his ability to fight injustice.",
	"https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
	"https://www.youtube.com/watch?v=EXeTwQWrcwY",
	christopher_nolan,
	christian_bale)

leonardo_diCaprio = media_person.Actor("Leonardo DiCaprio", "male", 
									   "avatar/Leonardo_DiCaprio.jpg")
inception = media.Movie(
	"Inception",
	"A thief who steals corporate secrets through use of dream-sharing \
	technology is given the inverse task of planting an idea into the \
	mind of a CEO.",
	"https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
	"https://www.youtube.com/watch?v=66TuSJo4dZM",
	christopher_nolan,
	leonardo_diCaprio)


ridley_scott = media_person.Director("Ridley Scott","male", 
									 "avatar/Ridley_Scott.jpg")
matt_damon = media_person.Actor("Matt Damon","male", 
								"avatar/Matt_Damon.png")
the_martian = media.Movie(
	"The Martian",
	"During a manned mission to Mars, Astronaut Mark Watney is presumed dead \
	after a fierce storm. With only meager supplies, he must draw upon his \
	ingenuity, wit and spirit to subsist and find a way to signal to Earth \
	that he is alive.",
	"https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
	"https://www.youtube.com/watch?v=ej3ioOneTy8",
	ridley_scott,
	matt_damon)

frank_darabont = media_person.Director("Frank Darabont","male",
									   "avatar/Frank_Darabont.jpg")
tim_robbins = media_person.Actor("Tim Robbins","male",
								 "avatar/Tim_Robbins.jpg")
the_shawshank_redemption = media.Movie(
	"The Shawshank Redemption",
	"Two imprisoned men bond over a number of years, finding solace and eventual \
	redemption through acts of common decency.",
	"https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
	"https://www.youtube.com/watch?v=6hB3S9bIaco",
	frank_darabont,
	tim_robbins)

rajkumar_hirani = media_person.Director("Rajkumar Hirani","male",
										"avatar/Rajkumar_Hirani.jpg")
aamir_khan = media_person.Actor("Aamir Khan", "male", 
								"avatar/Aamir_Khan.jpg")
threeIdiots = media.Movie(
	"3 Idiots",
	'''Two friends are searching for their long lost companion. They \
	revisit their college days and recall the memories of their friend \
	who inspired them to think differently, even as the rest of the world \
	called them "idiots".''',
	"https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
	"https://www.youtube.com/watch?v=xvszmNXdM4w",
	rajkumar_hirani,
	aamir_khan)

movies = [interstellar, the_dark_king, inception,
		  the_martian, the_shawshank_redemption, threeIdiots]
fresh_tomatoes.open_movies_page(movies)