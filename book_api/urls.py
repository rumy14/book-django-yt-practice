
from django.urls import path
from book_api.views import BookList, BookCreate
urlpatterns = [
    #path('', book_create),
    #path('list/', book_list),
    path('list/', BookList.as_view()),
    path('', BookCreate.as_view()),
    #path('<int:pk>', book)
]
