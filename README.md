# Classic Snake Game in Pygame

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.0%2B-green.svg?logo=python&logoColor=white)](https://www.pygame.org/)
[![Game](https://img.shields.io/badge/Game-Arcade%20Classic-yellow.svg)](#features)
[![Audio](https://img.shields.io/badge/Audio-SFX%20Enabled-blueviolet.svg)](#audio--assets)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A polished recreation of the classic arcade **Snake** game built with Python and **Pygame**. Features toroidal borderless screen wrapping, dynamic sound effects, persistent session high-score tracking, retro typography, and instantaneous pause mechanics.

---

## Game Mechanics & Logic

- **Grid Coordinates**: $20 \times 20$ discrete grid divisions rendered across an $800 \times 800$ pixel window ($40 \times 40$ px per cell).
- **Toroidal Screen Wrapping**: The snake seamlessly wraps around all four screen edges modulo the grid dimensions:
  $$x_{t+1} = (x_t + \Delta x) \pmod{20}, \quad y_{t+1} = (y_t + \Delta y) \pmod{20}$$
- **Anti-Reverse Direction Guard**: Prevents accidental self-collision when pressing the direct opposite movement key:
  $$|\text{direction}_{\text{new}} - \text{direction}_{\text{prev}}| \neq 2$$
- **Self-Collision Detection**: Evaluates coordinate occupancy; when the head index count in the snake body exceeds 1, death audio plays and game state resets.
- **Score System**: Live score tracking with session high-score persistence.

---

## Controls

| Key | Action |
| :--- | :--- |
| **`W`** | Move Up |
| **`A`** | Move Left |
| **`S`** | Move Down |
| **`D`** | Move Right |
| **`ESC`** | Toggle Pause / Resume |

---

## Audio & Assets

- `eat.wav`: Chime sound played upon food ingestion.
- `dead.wav`: Crash effect played on self-collision.
- `GamePlayed.ttf`: Retro arcade font rendering HUD score and pause overlays.

---

## Quickstart

```bash
git clone https://github.com/FortunateSpy5/snake-pygame.git
cd snake-pygame
pip install -r requirements.txt
python main.py
```

---

## License

This project is licensed under the [MIT License](LICENSE).
