from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main.views import *


router = routers.SimpleRouter()
router.register(r'management', DirectorViewSet, basename="management")
router.register(r'announcement', NotificationViewSet, basename="announcements")
router.register(r'news', NewViewSet, basename="news")
router.register(r'about', AboutViewSet, basename="about")
router.register(r'system', SystemViewSet, basename="system")
router.register(r'subsystem', SubsystemViewSet, basename="subsystem")
router.register(r'article', ArticleViewSet, basename="article")
router.register(r'comment', CommentViewSet, basename="comment")


urlpatterns = [
    path('', include(router.urls)),
]
