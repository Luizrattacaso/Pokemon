# 🐉 Pokémon Viewer

Aplicativo desktop em Python que exibe informações, imagem e movimentos dos Pokémons usando uma interface gráfica com **Tkinter**, consumindo dados via API externa através de módulos auxiliares (`get_pokemon_info`, `description`, `carregar_imagem_online`).

---

## Funcionalidades

- Exibe informações do Pokémon inicial **Dragonite** ao abrir.
- Permite buscar outros Pokémons por nome.
- Mostra:
  - Nome, tipo e ID
  - Imagem oficial
  - Descrição (texto)
  - Altura (em metros)
  - Peso (em kg)
  - Até 5 movimentos (moves)
- A cor de fundo muda conforme o tipo do Pokémon (cores definidas por tipo).

---

## 🧰 Tecnologias

- **Python 3.x**  
- **Tkinter** (interface gráfica)
- **Pillow** (manipulação de imagens)
- Módulos auxiliares (importados de `utils.py`):
  - `get_pokemon_info(nome)` → retorna JSON com dados do Pokémon
  - `description(nome)` → retorna texto descritivo
  - `carregar_imagem_online(nome)` → retorna imagem como `PhotoImage`

---

## ⚙️ Instalação e execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/Luizrattacaso/Pokemon.git
   cd Pokemon

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Certifique-se de que os arquivos `utils.py` e a pasta `icon/` estejam presentes.

4. Execute:

   ```bash
   python main.py
   ```

---

## 🖼️ Exemplo de uso

* Ao iniciar, exibe Dragonite:

  * ID: `#149`
  * Tipo: *Dragon*
  * Altura, peso e até 5 movimentos
* Pesquise outro Pokémon digitando o nome (ex: “Pikachu”) e clicando em **Search**. O layout é atualizado em tempo real.

---

## 📁 Estrutura sugerida

```
Pokemon/
├── main.py               ←script principal
├── utils.py              ←funções de API, descrição, imagem
├── icon/
│   └── cabeca-pikachu.png
└── README.md
```

---

## 🎨 Cores por tipo

Exemplos de cores definidas no dicionário `cores_tipos`:

| Tipo     | Cor (hex) |
| -------- | --------- |
| Normal   | `#A8A77A` |
| Fire     | `#EE8130` |
| Dragon   | `#7C5AD2` |
| Electric | `#F7D02C` |
| Water    | `#6390F0` |
| Grass    | `#7AC74C` |

---

## 🚀 Melhorias possíveis

* Buscar por ID ou múltiplos Pokémons.
* Scroll para descrições longas.
* Exibir imagem em alta resolução.
* Mostrar base stats, habilidades, etc.
* Melhor tratamento de erros (ex: Pokémon inválido, offline).

---

## 🤝 Contribuições & Licença

* **Contribuições bem-vindas**: abra uma issue ou envie um pull request.
* **Licença**: adicione um arquivo `LICENSE` ao projeto (ex: MIT, Apache 2.0).

---

## 🔍 Exemplo rápido de execução

```bash
git clone https://github.com/Luizrattacaso/Pokemon.git
cd Pokemon
pip install pillow requests
python main.py
```

Depois disso, digite o nome de um Pokémon e pressione **Search** para ver os dados atualizados na interface.


