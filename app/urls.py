from django.urls import path
from app import views
from app.apps import AppConfig

app_name = AppConfig.name

urlpatterns = [
    path("cards/", views.CardsView.as_view(), name="cards"),
    path("card/<int:pk>", views.CardDetailView.as_view(), name="card_history"),
    path("card/<int:pk>/delete", views.CardDeleteView.as_view(), name="card_delete"),
    path("card/<int:pk>/activate",
         views.card_activate, name="card_activate"),
    path("card/<int:pk>/deactivate", views.card_deactivate, name="card_deactivate"),
    path("card_generator/", views.CardGenerator.as_view(), name="card_generator"),

]
