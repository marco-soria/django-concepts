from django.urls import path
from django.http import HttpResponse
from .views import my_view, my_test_view, CarListView

urlpatterns = [
    #path("list", my_view),
    path("list", CarListView.as_view()),
    path("detail/<int:id>", my_test_view),
    path("brands/<str:brand_name>", my_test_view),
]