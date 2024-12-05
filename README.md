# Anime Recommendation System

## Project Overview

A Django-based REST API for anime recommendations, utilizing AniList GraphQL API and providing user-specific anime suggestions.

## Tech Stack

- Backend: Django
- Database: PostgreSQL
- Authentication: JWT (Django Simple JWT)
- API Integration: AniList GraphQL

## Prerequisites

- Python 3.9+
- PostgreSQL
- pip
- virtualenv (recommended)

## Setup and Installation

### 1. Clone the Repository


git clone https://github.com/akshatverma13/Xstage_Assignment
cd anime-recommendation-system


### 2. Create Virtual Environment


python -m venv venv
source venv/bin/activate # On Windows use \`venv\Scripts\activate\`


 3. Install Dependencies
    
pip install -r requirements.txt


### 4. Database Setup

# Create PostgreSQL database

psql -U postgres
CREATE DATABASE anime_recommendation_db;


### 5. Run Migrations


python manage.py makemigrations
python manage.py migrate


### 6. Create Superuser(Optional)


python manage.py createsuperuser


### 7. Run Development Server

python manage.py runserver


## API Endpoints

### Authentication Endpoints

| Endpoint                | Method | Description       | Request Body                          | Response                              |
| ----------------------- | ------ | ----------------- | ------------------------------------- | ------------------------------------- |
| \`/api/auth/register/\` | POST   | User Registration | \`{"username", "email", "password"}\` | User Details, Access & Refresh Tokens |
| \`/api/auth/login/\`    | POST   | User Login        | \`{"username", "password"}\`          | Access & Refresh Tokens               |
| \`/api/auth/refresh/\`  | POST   | Token Refresh     | \`{"refresh"}\`                       | New Access Token                      |

## Project Structure


anime_recommendation_project/
│
├── authentication/
│ ├── models.py # Custom user model
│ ├── serializers.py # User-related serializers
│ └── views.py # Authentication views
│
├── anime/
│ ├── models.py # Anime-related models
│ ├── views.py # Anime search views
│ └── anilist_client.py # AniList GraphQL client
│
└── recommendations/
└── views.py # Recommendation logic


#Use thunder client or postman to run all the APIs
REST API Endpoints:
/auth/register – Register a new user.
/auth/login – Login and retrieve a JWT token.
/anime/search – Search anime by name or genre.
/anime/recommendations – Fetch recommendations for the authenticated user.recommendations must come based on user prefrences
/user/preferences – Manage user preferences (e.g., favorite genres).
![image](https://github.com/user-attachments/assets/d48e0f0e-e161-489f-8bf9-08e0aa1b95f0)
![image](https://github.com/user-attachments/assets/53628a65-dd5d-4212-ac02-6c394e26a73f)
![image](https://github.com/user-attachments/assets/47d7c22e-33a0-406c-9ca7-80c0c352a499)
![image](https://github.com/user-attachments/assets/e0636415-4ba3-4773-ab43-7f7535150192)




