import requests

base_url = "https://pokeapi.co/api/v2/"

def description(pokemon):
    url = f"{base_url}pokemon-species/{pokemon.lower()}/"
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            english_entries = [
                entry["flavor_text"]
                for entry in data["flavor_text_entries"]
                if entry["language"]["name"] == "en"
            ]
            if english_entries:
                return english_entries[0]
        else:
            print(f"Something gone wrong. Status code: {response.status_code}")
    except:
        return None