import requests

def buscar_filmes(tipo="populares"):
    if tipo == "populares":
        url = "https://api.themoviedb.org/3/movie/popular?language=pt-BR&page=1"
    elif tipo == "mais_bem_avaliados":
        url = "https://api.themoviedb.org/3/discover/tv?include_adult=false&language=en-US&page=1&sort_by=vote_average.desc&vote_count.gte=200"
    elif tipo == "2010":
        url = "https://api.themoviedb.org/3/trending/movie/day"
    else:
        url = "https://api.themoviedb.org/3/movie/popular?language=pt-BR&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMDdhZmViZjNhYWM1YTZkZGY3ZmQyNGFlNjAwMTNlNyIsIm5iZiI6MTc3NDI4Njk5OC43NTQsInN1YiI6IjY5YzE3ODk2YWU3OTYyZjVjMmEyNTc0YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.aR6BOWzE8iMKEezDL75Bq3sPBkiON7aTV5oNC0FzkPk"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        dados = response.json()
        return dados.get("results", [])
    except requests.RequestException:
        return []