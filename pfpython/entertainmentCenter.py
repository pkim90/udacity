import media
import fresh_tomatoes

toyStory = media.Movie("Toy Story", "Stupid kid with shitty imagination", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print (toyStory.title)
print (toyStory.storyline)


avatar = media.Movie("Avatar", "Some blue skank trippin balls", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

print (avatar.title)
print (avatar.storyline)

amos = media.Movie("Famous Amos", "Clips of what Amos does", "https://www.facebook.com/photo.php?fbid=3805531532746&set=a.1417468752669.2057224.1111126103&type=3&theater", "https://www.youtube.com/watch?v=jP4DURAnStE")

movies = [toyStory, avatar, amos]

#fresh_tomatoes.open_movies_page(movies)

print (media.Movie.VALID_RATINGS)

print (media.Movie.__doc__)

print (media.Movie.__name__)

print (media.Movie.__module__)
