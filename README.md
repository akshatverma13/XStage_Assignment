
# Anime Recommendation System

## Project Overview

A Django-based REST API for anime recommendations, leveraging the AniList GraphQL API and providing user-specific anime suggestions based on preferences.

## Tech Stack

- **Backend**: Django, Django Rest Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (via Django Simple JWT)
- **API Integration**: AniList GraphQL API

## Prerequisites

- Python 3.9+
- PostgreSQL
- `pip` (Python package manager)
- `virtualenv` (recommended for environment isolation)

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/akshatverma13/Xstage_Assignment.git
cd anime-recommendation-system
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

#### Create a PostgreSQL Database
```sql
psql -U postgres
CREATE DATABASE anime_recommendation_db;
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

## API Endpoints

### Authentication Endpoints

| **Endpoint**             | **Method** | **Description**        | **Request Body**                       | **Response**                          |
|--------------------------|------------|------------------------|----------------------------------------|---------------------------------------|
| `/api/auth/register/`    | POST       | User Registration      | `{"username", "email", "password"}`    | User Details, Access & Refresh Tokens |
| `/api/auth/login/`       | POST       | User Login             | `{"username", "password"}`             | Access & Refresh Tokens               |
| `/api/auth/token/refresh/`| POST      | Token Refresh          | `{"refresh"}`                          | New Access Token                      |

### Anime-Related Endpoints

| **Endpoint**             | **Method** | **Description**                         | **Request Body**                      | **Response**                          |
|--------------------------|------------|-----------------------------------------|---------------------------------------|---------------------------------------|
| `/api/anime/search/`     | GET        | Search anime by name or genre           | `?query=<anime_name_or_genre>`        | List of matching anime                |
| `/api/anime/recommendations/` | GET   | Get recommendations for the user        | Authenticated request                 | List of recommended anime             |
| `/api/user/preferences/` | GET/POST   | View or update user preferences         | `{"favorite_genres": ["Action"]}`     | User's updated preferences            |

## Project Structure

```
anime_recommendation_project/
├── authentication/
│   ├── models.py           # Custom user models
│   ├── serializers.py      # User-related serializers
│   └── views.py            # Authentication views
│
├── anime/
│   ├── models.py           # Anime-related models
│   ├── views.py            # Anime search and recommendation views
│   └── anilist_client.py   # AniList GraphQL client for API integration
│
└── recommendations/
    └── views.py            # Recommendation logic
```

## Running the API

Use tools like [Postman](https://www.postman.com/) or [Thunder Client](https://www.thunderclient.com/) to test the API endpoints. You can also integrate the API with a simple frontend for better interaction.

## Additional Features

- **Minimal UI** (Optional): You can build a basic UI to interact with the API for testing.
- **Docker Support** (Optional): Containerize the application using Docker for easier deployment.

---

### Notes on AniList GraphQL Integration

Ensure you send a **POST** request to the AniList GraphQL API at `https://graphql.anilist.co`. Use headers and JSON payloads as required by the API documentation. Refer to [AniList Docs](https://docs.anilist.co/) for further details.

---

### Visual Examples (Optional)

If you have visuals, replace the placeholders below with actual screenshots:

- **User Registration**:
  ![User Registration Example](link_to_screenshot_1)

- **Anime Search**:
  ![Anime Search Example](link_to_screenshot_2)

- **Recommendations**:
  ![Recommendations Example](link_to_screenshot_3)

---

This README now has:
1. Corrected formatting for code blocks and commands.
2. Improved consistency in section headings and descriptions.
3. Expanded table details for API endpoints.
4. Placeholder notes for visuals to improve presentation.

Feel free to update links and add project-specific details as needed!
