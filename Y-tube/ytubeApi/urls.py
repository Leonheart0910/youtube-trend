
from django.urls import path, include
from ytubeApi import views
#admin은 장고가 가지고 있는 어드민 페이지
urlpatterns = [
    #홈으로 들어왔을때
    path('', views.index),
    path('create/',views.create),
    path('read/<id>/',views.read)
]
