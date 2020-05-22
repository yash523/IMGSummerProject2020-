from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bugtracker import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'apps', views.AppViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'bugs', views.BugViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'replies', views.ReplyViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]