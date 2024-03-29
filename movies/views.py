from ninja import Router
from .pydantic_models import MoviePydantic
from .serializers import MovieSerializer
from .models import Movie

movies_router = Router()


@movies_router.post("/movies")
def create_movie(request, data: MoviePydantic):
    movie_data = data.dict()
    # Create the movie object
    movie = Movie.objects.create(**movie_data)
    return {"status": "Movie created successfully", "movie": movie}


@movies_router.get("/movies")
def list_movies(request):
    # Fetch all movies from the database
    movies = Movie.objects.order_by("-ranking")
    serialized_movies = MovieSerializer(movies, many=True)
    serialized_data = serialized_movies.data

    return serialized_data
