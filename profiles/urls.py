from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.FeedViewsSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]