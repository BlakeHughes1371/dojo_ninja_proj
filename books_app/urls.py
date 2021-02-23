from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('createbook', views.createbook),
    path('books/<int:bookid>', views.books),
    path('addAuthortoBook/<int:bookid>',views.addAuthortoBook)
]
