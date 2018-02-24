import fresh_tomatoes
import media


# Movies with title, description, box art and trailer link

toy_story = media.Movie(
    "Toy Story",
    "The adventures of a boy and his toys that come to life.",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
)

avatar = media.Movie(
    "Avatar",
    "The adventures of a marine on an alien planet.",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
)

lion_king = media.Movie(
    "The Lion King",
    "The adventures of a young lion, named Simba.",
    "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
    "https://www.youtube.com/watch?v=4sj1MT05lAA"
)

rango = media.Movie(
    "Rango",
    "The adventures of a chameleon, named Rango.",
    "https://upload.wikimedia.org/wikipedia/en/6/6d/Rango2011Poster.jpg",
    "https://www.youtube.com/watch?v=qPJgbv1nHBw"
)

up = media.Movie(
    "Up",
    "The adventures of an elderly balloon salesman.",
    "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
    "https://www.youtube.com/watch?v=pkqzFUhGPJg"
)

finding_nemo = media.Movie(
    "Finding Nemo",
    "The adventures of a young clownfish, named Nemo.",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
    "https://www.youtube.com/watch?v=yDPRaVX2p8c"
)

movies = [toy_story, avatar, lion_king, rango, up, finding_nemo]

# Generate movie trailer website

fresh_tomatoes.open_movies_page(movies)
