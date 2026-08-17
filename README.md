# Snake

The classic arcade snake, built with Python's `turtle` graphics module and sound.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/) [![Turtle](https://img.shields.io/badge/turtle-graphics-2ea44f?style=flat-square)](https://docs.python.org/3/library/turtle.html)

---

## Play

```bash
git clone https://github.com/dhruvg0ya1/Snake-Game.git
cd Snake-Game
python Main.py
```

Arrow keys to steer. Eat the food, grow longer, do not hit the wall or yourself.

## How it is built

```
Main.py                  game loop, input binding, collision checks
components/
├── Snake.py             segment list, movement, growth
├── Food.py              random placement and respawn
├── Scoreboard.py        current score and persisted high score
└── hs.txt               high score, written between runs
sounds/                  eating, collision and background audio
```

Three collision cases drive the loop: food (grow and rescore), wall (reset), and
self-intersection (reset). The high score survives restarts by being written to
`components/hs.txt`.

## Requirements

Python 3.10+. `turtle` ships with the standard library, so there is nothing to
install.
