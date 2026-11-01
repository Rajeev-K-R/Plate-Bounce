# 🏓 Plate Bounce

A small arcade-style game built in **Python** using **Pygame**. A ball continuously moves and bounces within the game window, while the player controls a plate/paddle to keep the ball alive.

The project is a compact exercise in real-time game loops, collision handling, keyboard input, and 2D animation.

## ✨ Highlights

- Real-time Pygame game loop
- Ball movement and wall bouncing
- Player-controlled plate/paddle
- Collision-based gameplay
- Simple arcade-style objective: keep the ball alive

## 🧠 How It Works

The game repeatedly updates the position of the moving ball and redraws the scene.

At a high level:

1. Pygame creates the game window.
2. The player's plate is controlled through keyboard input.
3. The ball position is updated every frame.
4. When the ball reaches a boundary, its direction is changed to create a bounce.
5. Collision with the player's plate keeps the ball in play.
6. The display is refreshed continuously to create the animation.

The core idea is deliberately simple: combine **position updates + collision detection + user input + a continuous rendering loop** to produce an interactive game.

## 🛠️ Tech Stack

- **Python**
- **Pygame**

## ▶️ Run

Install Pygame:

```bash
pip install pygame
```

Then enter the game directory:

```bash
cd Plate-Bounce/Plate_bounce
```

Run the Python game file contained in that directory:

```bash
python <game_file>.py
```

> **Repository note:** The web-accessible repository listing exposes the `Plate_bounce/` directory but not the entry-file name. Replace `<game_file>.py` with the `.py` file in that directory.

## 🎮 Controls

Use the keyboard controls implemented by the game to move the plate/paddle and keep the ball in play.

## 🎥 Demo

A short gameplay recording can be added here:

> 🎬 **Demo:** *Add YouTube / Google Drive / GitHub-hosted demo link here*

For example:

```markdown
[▶️ Watch the Plate Bounce Demo](https://github.com/user-attachments/assets/6b8f8187-829d-4024-9d7b-242ee69705b3)

```

## 📌 Project Context

Built as a compact Python/Pygame project to practise interactive programming, animation, collision logic, and event-driven application design.

## 📄 License

Apache-2.0
