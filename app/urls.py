from django.urls import path
from app import views
from app.apps import AppConfig

app_name = AppConfig.name

urlpatterns = [
    path("cards/", views.CardsView.as_view(), name="Cards"),
    path("card/<int:pk>", views.CardDetailView.as_view(), name="Card History"),
]
