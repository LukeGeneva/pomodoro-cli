# Pomodoro Timer

A simple console-based Pomodoro Timer application written in Python. The timer
displays remaining time and plays a sound upon expiration.

## Features

- Countdown timer with 25-minute duration (default Pomodoro time)
- Plays a sound when the timer expires

## Requirements

- Python 3.6+

## Usage

To use the Pomodoro Timer, run the following command in your terminal:

```bash
python pomodoro.py start
```

This will start the 25-minute timer. The remaining time will be displayed using
large ASCII art numbers, and the cursor will be hidden while the timer is
running. When the timer expires, a sound will play, and the cursor will
reappear.

## Platform Compatibility

The Pomodoro Timer should work on Linux and macOS. However, the sound playback
functionality may not work on all systems due to differences in the available
sound libraries and system commands. Please modify the `play_sound` function if
necessary to adapt it to your system.

## License

This project is released under the ISC License. See the [LICENSE](LICENSE) file
for details.

