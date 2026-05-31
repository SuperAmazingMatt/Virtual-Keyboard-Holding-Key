# AutoKey Pro Max: Human-Like Keyboard Macro

An advanced, highly customizable Python macro script that holds a primary key while simulating human-like randomized secondary key presses. 

Unlike basic auto-clickers, this script utilizes "stutter-step" logic and random time variances to closely mimic actual human kinetic input, making it ideal for grinding or farming in single-player and casual games.

## ✨ Features
* **Continuous Hold:** Locks down a primary key (e.g., `w`) without breaking the input.
* **Random Interruption:** Randomly taps secondary keys (e.g., `space`, `r`) at randomized intervals.
* **Human-Like Stutter Step:** If the macro randomly selects the key that is currently being held, it physically simulates a human finger lifting and dropping the key with a realistic reaction time delay (0.12s - 0.25s).
* **GUI Interface:** Built-in Tkinter interface for easy parameter adjustments on the fly.

## ⚠️ Disclaimer & Warning
**This tool is for educational purposes and single-player/casual use only.** Because this script utilizes Windows software injection (`LLKHF_INJECTED`), it will be immediately flagged by kernel-level anti-cheat systems (such as Vanguard, Ricochet, BattlEye, or Easy Anti-Cheat). Do not use this in highly competitive multiplayer games, or you risk an account ban. I am not responsible for any banned accounts or actions taken against you for using this software.

## 🛠️ Prerequisites
To run or compile this code, you must have Python installed on your Windows machine, along with the following library:
```bash
pip install keyboard
