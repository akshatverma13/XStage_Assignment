from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from anime.anilist_client import AniListClient

class AnimeRecommendationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        favorite_genres = user.favorite_genres

        # Simple recommendation logic based on user's favorite genres
        recommendations = []
        for genre in favorite_genres:
            result = AniListClient.search_anime(query=genre, per_page=3)
            recommendations.extend(result['data']['Page']['media'])

        return Response(recommendations)