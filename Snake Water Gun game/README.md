## 🐍💧🔫 Snake Water Gun – Python Game

A simple and fun Snake-Water-Gun game made in Python!
This game works similarly to Rock-Paper-Scissors, but with a twist. Both the computer and the user choose one of the three options:

- Snake (s)

- Water (w)

- Gun (g)

The computer selects its option randomly, and the result is shown as Win, Lose, or Draw based on the rules of the game.

---

## 🎮 Game Rules

| User vs Computer    | Outcome                            |
| ------------------- | ---------------------------------- |
| Snake vs Water      | Snake drinks water → **User Wins** |
| Snake vs Gun        | Gun kills snake → **User Loses**   |
| Water vs Gun        | Gun sinks in water → **User Wins** |
| If both choose same | **Draw**                           |

---

## 🧠 How It Works

- The computer uses random.choice() to pick snake, water, or gun.

- The user enters:

  - s for Snake

  - w for Water

  - g for Gun

- The program compares both choices and prints:

  - "You Win!"

  - "You Lose!"

  - "It's a Draw!"

---

## ✅ Features

- Simple and beginner-friendly

- Uses Python’s random module

- Clear input system (s, w, g)

- Instant game result