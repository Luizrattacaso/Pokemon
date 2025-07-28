import requests
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(pokemon):
    url = f"{base_url}pokemon/{pokemon}"
    response = requests.get(url)

    try: 
        if response.status_code == 200:
            information = response.json()
            return information
        else:
            return print(f"Status code: {response.status_code}")

    except Exception as Error:
        print("Error: {Error}")

def details():
    name = input("Enter a pokemon name for better informations: ")
    try:
        pokemon_info = get_pokemon_info(name)
        print(f"Name: {pokemon_info["name"].capitalize()}")
        print(f"ID: {pokemon_info["id"]}")
        print(f"weight : {pokemon_info["weight"]}")
        print(f"height : {pokemon_info["height"]}")
        print()
        choose = input("Do you want to search more pokemon data? (y/n)")

        if "Y" in choose[0] or "y" in choose[0]:
            print("hello")
        else:
            print("Finishing the program...")
            print()
    except Exception as error:
        print(f"Something gone wrong!\nErro: {error}")
    
details()