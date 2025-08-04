# 🐉 Pokémon Viewer

A desktop Python app that displays information, image, and moves of Pokémon using a graphical interface built with Tkinter, consuming data from an external API via helper modules (get_pokemon_info, description, load_image).

---

## Features

- Displays initial Pokémon Dragonite on startup.
- Allows searching for other Pokémon by name.
- Shows:
  - Name, type, and ID
  - Official image
  - Description text
  - Height (in meters)
  - Weight (in kg)
  - Up to 5 moves
- Background color changes according to the Pokémon's type (colors defined by type).

---

## 🧰 Technologies

- **Python 3.x**  
- **Tkinter** (graphical interface)
- **Pillow** (mage handling)
- Helper modules (imported from `utils.py`):
  - `get_pokemon_info(nome)` → returns a JSON with Pokémon data
  - `description(nome)` → returns a descriptive text
  - `carregar_imagem_online(nome)` → returns image as `PhotoImage`

---

## ⚙️ Installation & Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/Luizrattacaso/Pokemon.git
   cd Pokemon

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Make sure the utils.py file and icon/ folder are present.

4. Run the app:

   ```bash
   python main.py
   ```

---

## 🖼️ Usage Example

* It shows Dragonite as initial pokemon:

  * ID: `#149`
  * Type: *Dragon*
  * Height, weight, and up to 5 moves
* Search for another Pokémon by typing its name (e.g., “Pikachu”) and clicking Search. The layout updates in real time.

---

## 📁 Suggested Structure

```
Pokemon/
├── main.py               ←main script
├── utils.py              ←API, description, image functions
├── icon/
│   └── cabeca-pikachu.png
└── README.md
```

---

## 🎨 Type Colors

Examples of colors defined in the cores_tipos dictionary:

| Tipo     | Cor (hex) |
| -------- | --------- |
| Normal   | `#A8A77A` |
| Fire     | `#EE8130` |
| Dragon   | `#7C5AD2` |
| Electric | `#F7D02C` |
| Water    | `#6390F0` |
| Grass    | `#7AC74C` |

---

## 🚀 Possible Improvements

* Search by ID or multiple Pokémon.
* Scroll support for long descriptions.
* Display high-resolution images.
* Show base stats, abilities, etc.
* Better error handling (e.g., invalid Pokémon, offline status).

---

## 🤝 Contributions & License

* **Contributions are welcome**: open an issue or submit a pull request.
* **License**: consider adding a LICENSE file to the project (e.g., MIT, Apache 2.0).

---

## 🔍 Quick Run Example

```bash
git clone https://github.com/Luizrattacaso/Pokemon.git
cd Pokemon
pip install pillow requests
python main.py
```

After that, enter a Pokémon name and press Search to see the updated data in the interface.
