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
        return f"Error: {Error}"

def description(pokemon):
    url = f"{base_url}pokemon-species/{pokemon.lower()}/"
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            description = data["flavor_text_entries"][0]["flavor_text"]
            if description == None:
                return f"it's not possible to search\nfor information about {pokemon}"
            else:
                return description
        else:
            print(f"Something gone wrong. Status code: {response.status_code}")
    except ValueError as v:
        return f"Value Error: {v}"
    except Exception as e:
        return f"Error: {e}"
    

def get_evolution_chain(chain_url_or_id):
    if isinstance(chain_url_or_id, int):
        url = f"https://pokeapi.co/api/v2/evolution-chain/{chain_url_or_id}/"
    else:
        url = chain_url_or_id

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erro ao obter a cadeia de evolução.\nErro : {response.status_code}")
        return

    data = response.json()
    print("Linha de Evolução:")
    print("="*50)
    show_evolution_chain(data["chain"])

def show_evolution_chain(chain, depth=0):
    indent = "  " * depth
    current_pokemon = chain["species"]["name"].capitalize()
    print(f"{indent}→ {current_pokemon}")

    for evolution in chain["evolves_to"]:
        # Detalhes da evolução
        details = evolution["evolution_details"][0] if evolution["evolution_details"] else None
        trigger = details["trigger"]["name"] if details else "level-up"

        method = ""
        if trigger == "use-item" and details.get("item"):
            method = f" (usando {details['item']['name'].replace('-', ' ').title()})"
        elif trigger == "trade":
            if details.get("held_item"):
                method = f" (trocando com item: {details['held_item']['name'].replace('-', ' ').title()})"
            else:
                method = " (trocando)"
        elif trigger == "level-up":
            if details and details.get("min_level"):
                method = f" (nível {details['min_level']})"
            else:
                method = " (nível)"
        elif trigger == "shed":
            method = " (shed)"
        # Adicione outros triggers conforme necessário

        print(f"{indent}  ↳ Evolui por: {trigger.replace('-', ' ').title()}{method}")

        show_evolution_chain(evolution, depth + 1)

#get_evolution_chain(25)

description("dragonite")