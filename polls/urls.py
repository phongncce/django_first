from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("details/<int:question_id>/", views.detail, name="detail"),
    path("results/<int:question_id>/", views.results, name="result"),
    path("vote/<int:question_id>", views.vote, name="vote"),
]
