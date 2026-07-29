# Pokémon Viewer

A desktop Python app that displays information, image, and moves of Pokémon using a graphical interface built with Tkinter, consuming data from an external API via helper modules (get_pokemon_info, description, load_image).


## Features

- Displays pokeball on startup.
- Allows searching for other Pokémon by name.
- Shows:
  - Name, type, and ID
  - Official image
  - Description text
  - Height (in meters)
  - Weight (in kg)
  - Up to 5 moves
- Background color changes according to the Pokémon's type (colors defined by type).

## Technologies

- **Python 3.x**  
- **Tkinter** (graphical interface)
- **Pillow** (mage handling)
- Helper modules (imported from `program`):
  - `get_pokemon_info(name)` → returns a JSON with Pokémon data
  - `description(name)` → returns a descriptive text
  - `load_image(name)` → returns image as `PhotoImage`

## Installation & Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/Luizrattacaso/Pokemon.git
   cd Pokemon

2. Install dependencies:

   2.1 Create and activate a virtual environment (highly recommended):
     
      ```
      python -m venv venv
      source venv/bin/activate  # On Windows use: venv\Scripts\activate
      ```
    
       ```
       pip install -r requirements.txt
       ```
  or use:
   ```
   pip install requests
   pip install pillow
   ```

3. Run the app:

   ```bash
   python main.py
   ```

## Usage Example
- On startup, a placeholder Pokéball is displayed.
- Search for a Pokémon by typing its name (e.g., "Pikachu") or typing an ID (e.g. 25) and clicking Search or pressing Enter.
- The app instantly updates to show:

    ID and Type
    Height and weight
    Up to 5 moves
    Pokémon image and description

The interface background color updates to match the Pokémon's type

## Suggested Structure

```
Pokemon/
├── .gitignore
├── LICENSE
├── README.md
├── main.py                 # Main entry point script
├── requirements.txt        # Python dependencies
├── public/                 # Static assets
│   └── icone-pikachu.png   # Application icon
└── src/                    # Source code directory
    ├── __init__.py
    ├── program/            # UI and window management
    │   ├── __init__.py
    │   ├── frame_window.py
    │   └── main_frame.py
    └── utils/              # Helper functions and API calls
        ├── __init__.py
        ├── check_id.py
        ├── get_description.py
        ├── get_pokeball_image.py
        ├── get_pokemon_info.py
        └── load_pokemon_image.py
```

---

## Type Colors

Examples of colors defined in the cores_tipos dictionary:

| Tipo     | Cor (hex) |
| -------- | --------- |
| Normal   | `#A8A77A` |
| Fire     | `#EE8130` |
| Dragon   | `#7C5AD2` |
| Electric | `#F7D02C` |
| Water    | `#6390F0` |
| Grass    | `#7AC74C` |

## Possible Improvements

* Search by ID or multiple Pokémon.
* Scroll support for long descriptions.
* Show base stats, abilities, etc.
* Better error handling (e.g., invalid Pokémon, offline status).

## Contributions & License

* **Contributions are welcome**: open an issue or submit a pull request.
* **License**: consider adding a LICENSE file to the project (e.g., MIT, Apache 2.0).

## Quick Run Example

```bash
git clone https://github.com/Luizrattacaso/Pokemon.git
cd Pokemon
pip install pillow requests
python main.py
```

After that, enter a Pokémon name and press Search to see the updated data in the interface.
