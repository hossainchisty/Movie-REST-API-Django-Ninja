from django.urls import path
from ninja import NinjaAPI
from .views import movies_router

app_name = "movies"

api = NinjaAPI()

api.add_router("/api/v1", movies_router)

urlpatterns = [
    path("", api.urls),
]
