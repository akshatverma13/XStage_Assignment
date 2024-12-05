# anime_recommendation_project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Import the views explicitly
from authentication.views import UserRegistrationView, UserPreferencesView
from recommendations.views import AnimeRecommendationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/', UserRegistrationView.as_view(), name='register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/preferences/', UserPreferencesView.as_view(), name='user_preferences'),
    path('api/anime/recommendations/', AnimeRecommendationView.as_view(), name='anime_recommendations'),
]