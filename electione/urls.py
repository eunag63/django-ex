from django.urls import path
from . import views
#앱 접속시 electione에서 접속해라
urlpatterns = [
    path('', views.index),
    path('areas/<str:area>/', views.areas),
    path('polls/<int:poll_id>', views.polls),
    path('areas/<str:area>/results/', views.results),
    path('candidates/<str:name>/', views.candidates)
]
