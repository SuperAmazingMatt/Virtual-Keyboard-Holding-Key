import tkinter as tk
import keyboard
import random
import time
import threading

holding = False

def random_press_loop(keys_list, min_w, max_w, base_tap, tap_var):
    """Runs in the background, handling the random waiting and random tapping."""
    target_key = key_input.get().lower() 
    
    while holding:
        # 1. Wait time BETWEEN presses
        wait_time = random.uniform(min_w, max_w)
        time.sleep(wait_time)
        
        if not holding:
            break
            
        # 2. Pick a random key
        if len(keys_list) > 0:
            rand_key = random.choice(keys_list)
            
            # 3. THE SMART HUMAN LOGIC
            if rand_key == target_key:
                # If tapping the HELD key: Simulate the same finger lifting and dropping.
                # A real human takes about 0.12 to 0.25 seconds to lift a heavy finger and press it back down.
                human_lift_time = random.uniform(0.12, 0.25)
                
                keyboard.release(target_key)
                time.sleep(human_lift_time) # The finger is in the air...
                keyboard.press(target_key)  # The finger drops back down!
                
                print(f"Human stutter on '{rand_key}' (Finger lifted for {human_lift_time:.3f} seconds)")
                
            else:
                # If tapping a DIFFERENT key: Normal fast tap calculation.
                actual_tap_duration = base_tap + random.uniform(-tap_var, tap_var)
                if actual_tap_duration < 0.01:
                    actual_tap_duration = 0.01 
                    
                keyboard.press(rand_key)
                time.sleep(actual_tap_duration) # The second finger taps the key
                keyboard.release(rand_key)
                
                print(f"Fast tap on '{rand_key}' for {actual_tap_duration:.3f} seconds.")


def start_holding():
    global holding
    
    target_key = key_input.get().lower()
    rand_keys_str = random_keys_input.get().lower()
    
    # Clean up the random keys into a list
    rand_keys = [k.strip() for k in rand_keys_str.split(',') if k.strip() != ""]
    
    # Grab all the timing numbers and ensure they are valid decimals
    try:
        min_w = float(min_wait_input.get())
        max_w = float(max_wait_input.get())
        base_tap = float(base_tap_input.get())
        tap_var = float(tap_var_input.get())
    except ValueError:
        status_label.config(text="Status: Times must be numbers!", fg="red")
        return

    if target_key != "" and not holding:
        keyboard.press(target_key)
        holding = True
        status_label.config(text=f"Status: HOLDING '{target_key}'", fg="green")
        
        # Start the background loop with our new tap variables
        t = threading.Thread(target=random_press_loop, args=(rand_keys, min_w, max_w, base_tap, tap_var), daemon=True)
        t.start()

def stop_holding():
    global holding
    target_key = key_input.get().lower()
    
    if holding:
        keyboard.release(target_key)
        holding = False
        status_label.config(text="Status: Stopped", fg="red")

# Set up the hotkeys
keyboard.add_hotkey('f1', start_holding)
keyboard.add_hotkey('f2', stop_holding)

def on_close():
    stop_holding() 
    root.destroy()

# --- BUILD THE VISUAL WINDOW ---
root = tk.Tk()
root.title("AutoKey Pro Max")
root.geometry("380x600") # Made the window taller to fit the new boxes

# 1. Main Key
tk.Label(root, text="Main Key to Hold:", font=("Segoe UI", 10, "bold")).pack(pady=(15, 0))
key_input = tk.Entry(root, font=("Segoe UI", 12), justify="center", width=10)
key_input.insert(0, "w")
key_input.pack(pady=5)

# 2. Random Keys
tk.Label(root, text="Random Keys to Press (comma separated):", font=("Segoe UI", 10, "bold")).pack(pady=(10, 0))
random_keys_input = tk.Entry(root, font=("Segoe UI", 12), justify="center", width=25)
random_keys_input.insert(0, "space, r")
random_keys_input.pack(pady=5)

# --- NEW SECTION: TAP DURATION ---
tk.Label(root, text="--- How long to hold the random key ---", fg="gray").pack(pady=(15, 5))

# Base Tap
tk.Label(root, text="Base Tap Duration (Seconds):", font=("Segoe UI", 9, "bold")).pack()
base_tap_input = tk.Entry(root, font=("Segoe UI", 11), justify="center", width=10)
base_tap_input.insert(0, "0.1") # 1/10th of a second is a normal human tap
base_tap_input.pack(pady=2)

# Variance
tk.Label(root, text="Tap Variance (+/- Seconds):", font=("Segoe UI", 9, "bold")).pack()
tap_var_input = tk.Entry(root, font=("Segoe UI", 11), justify="center", width=10)
tap_var_input.insert(0, "0.05") 
tap_var_input.pack(pady=2)

# --- OLD SECTION: WAIT TIME ---
tk.Label(root, text="--- Time to wait between presses ---", fg="gray").pack(pady=(15, 5))

# Min Wait
tk.Label(root, text="Min Wait Time (Seconds):", font=("Segoe UI", 9, "bold")).pack()
min_wait_input = tk.Entry(root, font=("Segoe UI", 11), justify="center", width=10)
min_wait_input.insert(0, "1")
min_wait_input.pack(pady=2)

# Max Wait
tk.Label(root, text="Max Wait Time (Seconds):", font=("Segoe UI", 9, "bold")).pack()
max_wait_input = tk.Entry(root, font=("Segoe UI", 11), justify="center", width=10)
max_wait_input.insert(0, "5")
max_wait_input.pack(pady=2)

# Instructions & Status
tk.Label(root, text="Press F1 to Start  |  Press F2 to Stop", font=("Segoe UI", 9, "italic")).pack(pady=(20, 5))
status_label = tk.Label(root, text="Status: Waiting...", font=("Segoe UI", 12, "bold"))
status_label.pack(pady=5)

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()