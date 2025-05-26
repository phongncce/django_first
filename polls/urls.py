from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("details/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("results/<int:pk>/", views.ResultsView.as_view(), name="result"),
    path("vote/<int:question_id>", views.vote, name="vote"),
]
