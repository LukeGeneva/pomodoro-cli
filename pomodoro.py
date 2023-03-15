#!/usr/bin/env python3

import time
import os
import sys

def play_sound():
    if sys.platform.startswith('linux'):
        os.system('play -nq -t alsa synth {} sine {}'.format(1, 1000))
    elif sys.platform.startswith('darwin'):
        os.system('say "Pomodoro time is up"')

def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"Time Remaining: {minutes:02d}:{seconds:02d}"

def start_pomodoro(minutes):
    hide_cursor()
    end_time = time.time() + minutes * 60
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        sys.stdout.write("\r" + format_time(remaining_time))
        sys.stdout.flush()
        time.sleep(1)
    play_sound()
    show_cursor()
    print("\nTime's up!")

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "start":
            start_pomodoro(25)
        elif command == "break":
            start_pomodoro(5)
        else:
            print("Invalid command.")
    else:
        print("Usage: python pomodoro.py start")
