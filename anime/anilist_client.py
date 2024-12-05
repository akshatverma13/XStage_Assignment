import requests

class AniListClient:
    BASE_URL = 'https://graphql.anilist.co'

    @classmethod
    def search_anime(cls, query, page=1, per_page=10):
        graphql_query = '''
        query ($search: String, $page: Int, $perPage: Int) {
            Page(page: $page, perPage: $perPage) {
                media(search: $search, type: ANIME) {
                    id
                    title { romaji english native }
                    genres
                    averageScore
                    popularity
                }
            }
        }
        '''
        
        variables = {
            'search': query,
            'page': page,
            'perPage': per_page
        }

        response = requests.post(cls.BASE_URL, json={'query': graphql_query, 'variables': variables})
        return response.json()