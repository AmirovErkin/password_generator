from django.urls import path
from . import views
urlpatterns = [
    path('easy/', views.easy_password)
]
