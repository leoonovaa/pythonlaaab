import requests

def load_credentials(filename):
    credentials = {}
    with open(filename) as f:
        for line in f:
            key, value = line.strip().split("=")
            credentials[key] = value
    return credentials.get("CLIENT_ID"), credentials.get("CLIENT_SECRET")

def get_access_token(client_id, client_secret):
    resp = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret)
    )
    return resp.json().get("access_token") if resp.status_code == 200 else None

def search_track(query, token):
    resp = requests.get(
        "https://api.spotify.com/v1/search",
        headers={"Authorization": f"Bearer {token}"},
        params={"q": query, "type": "track", "limit": 5}
    )
    if resp.status_code == 200:
        tracks = resp.json().get("tracks", {}).get("items", [])
        if not tracks:
            print("За вашим запитом результатів немає.")
        for t in tracks:
            print(f"Назва треку: {t['name']}\nВиконавець: {', '.join(a['name'] for a in t['artists'])}\nАльбом: {t['album']['name']}\nПосилання: {t['external_urls']['spotify']}\n")
    elif resp.status_code == 401:
        print("Помилка авторизації. Спробуйте отримати новий токен.")
    elif resp.status_code == 429:
        print("Перевищено ліміт запитів.")
    else:
        print(f"Сталася помилка: статус {resp.status_code}")

def main():
    client_id, client_secret = load_credentials("444.env")
    if not client_id or not client_secret:
        print("Не вдалося завантажити Client ID і Client Secret.")
        return
    query = input("Введіть назву пісні або виконавця: ")
    token = get_access_token(client_id, client_secret)
    if token:
        search_track(query, token)

if __name__ == "__main__":
    main()
