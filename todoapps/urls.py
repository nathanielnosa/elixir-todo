from django.urls import path
from . import views
urlpatterns = [
    path('create/',views.TodoCreateGetView.as_view()),
    path('retrieve/',views.TodoCreateGetView.as_view())
]