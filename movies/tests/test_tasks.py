import pytest
from movies.tasks import update_movie_rankings
from unittest.mock import patch
from datetime import timedelta
from movies.models import Movie
from django.utils import timezone


@pytest.mark.django_db
def test_update_movie_rankings_task():
    movie1 = Movie.objects.create(title="Movie 1", status="coming_up", ranking=50)
    movie2 = Movie.objects.create(title="Movie 2", status="coming_up", ranking=60)

    # Patch timezone.now to simulate time
    with patch("django.utils.timezone.now") as mock_now:
        # Set mock time to now
        mock_now.return_value = timezone.now()

        # Call the Celery task
        update_movie_rankings.delay()

    # Fetch movies after the task execution
    updated_movie1 = Movie.objects.get(pk=movie1.pk)
    updated_movie2 = Movie.objects.get(pk=movie2.pk)

    # Check if rankings are updated correctly
    assert updated_movie1.ranking == 60
    assert updated_movie2.ranking == 70

    # Patch timezone.now again to simulate 5 minutes later
    with patch("django.utils.timezone.now") as mock_now:
        # Set mock time to 5 minutes later
        mock_now.return_value += timedelta(minutes=5)

        # Call the Celery task again
        update_movie_rankings.delay()

    # Fetch movies after the second task execution
    updated_movie1 = Movie.objects.get(pk=movie1.pk)
    updated_movie2 = Movie.objects.get(pk=movie2.pk)

    # Check if rankings are updated correctly after 5 minutes
    assert updated_movie1.ranking == 70
    assert updated_movie2.ranking == 80
