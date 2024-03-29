import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from movies.models import Movie

class TestMovieAPI:
    client = APIClient()

    def test_create_movie(self):
        movie_data = {
            "title": "Test Movie",
            "description": "This is a test movie",
            "release_date": "2024-03-28T12:00:00Z",
        }

        response = self.client.post(
            reverse("movies:create_movie"),
            data=json.dumps(movie_data),
            content_type="application/json",
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert Movie.objects.filter(title=movie_data["title"]).exists()

    def test_list_movies(self):
        response = self.client.get(reverse("movies:list_movies"))

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.data, list)