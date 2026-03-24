from gtts import gTTS
import os

# Create a directory for the sound files
output_dir = "sounds"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- NEW ---
# Descriptive names for each candy type
candy_objects = {
    'red': 'strawberry',
    'purple': 'grapes',
    'blue': 'diamond',
    'green': 'apple',
    'orange': 'peach',
    'yellow': 'star'
}

super_candy_objects = {
    'explosion': 'explosion'
}

print("Generating sound files for candy objects...")

# Generate sounds for regular candies
for color, name in candy_objects.items():
    try:
        tts = gTTS(text=name, lang='en', tld='co.uk', slow=False)
        file_path = os.path.join(output_dir, f"{color}.mp3")
        tts.save(file_path)
        print(f"Successfully generated sound for '{name}' at {file_path}")
    except Exception as e:
        print(f"Failed to generate sound for '{name}': {e}")

# Generate sounds for super candies
for color, name in super_candy_objects.items():
    try:
        tts = gTTS(text=name, lang='en', tld='co.uk', slow=False)
        file_path = os.path.join(output_dir, f"{color}_super.mp3")
        tts.save(file_path)
        print(f"Successfully generated sound for '{name}' at {file_path}")
    except Exception as e:
        print(f"Failed to generate sound for '{name}': {e}")


print("\nAll sound files generated.")

try:
    tts = gTTS(text="You win!", lang='en', tld='co.uk', slow=False)
    file_path = os.path.join(output_dir, "you_win.mp3")
    tts.save(file_path)
    print(f"Successfully generated sound for 'You win!' at {file_path}")
except Exception as e:
    print(f"Failed to generate sound for 'You win!': {e}")

try:
    tts = gTTS(text="nice", lang='en', tld='co.uk', slow=False)
    file_path = os.path.join(output_dir, "nice.mp3")
    tts.save(file_path)
    print(f"Successfully generated sound for 'nice' at {file_path}")
except Exception as e:
    print(f"Failed to generate sound for 'nice': {e}")
