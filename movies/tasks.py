from celery import shared_task
from datetime import timedelta
from movies.models import Movie


@shared_task
def update_movie_rankings():
    # Fetch movies with status="coming_up"
    coming_up_movies = Movie.objects.filter(status="coming_up")

    # Increment ranking by 10 for each coming up movie
    for movie in coming_up_movies:
        movie.ranking += 10
        movie.save()

    # Schedule task to run again in 5 minutes
    update_movie_rankings.apply_async(countdown=300)  # 300 seconds = 5 minutes
