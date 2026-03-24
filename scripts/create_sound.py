from gtts import gTTS
import os

# --- NEW ---
# A dictionary of available English accents and their TLDs
accent_profiles = {
    "1": {"name": "US English", "tld": "com"},
    "2": {"name": "UK English", "tld": "co.uk"},
    "3": {"name": "Australian English", "tld": "com.au"},
    "4": {"name": "Canadian English", "tld": "ca"},
    "5": {"name": "Indian English", "tld": "co.in"},
    "6": {"name": "Irish English", "tld": "ie"},
    "7": {"name": "South African English", "tld": "co.za"},
}

# Create a directory for the sound files
output_dir = "sounds"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- MODIFIED ---
# Get user input for the accent profile
print("Please select an English accent profile:")
for key, profile in accent_profiles.items():
    print(f"{key}: {profile['name']}")

choice = input("Enter the number for your choice: ")
selected_tld = accent_profiles.get(choice, {"tld": "com"})["tld"]


# Get user input for text and filename
text_to_speak = input("\nEnter the word or phrase to convert to speech: ")
file_name = input("Enter the desired file name (without .mp3 extension): ")

if text_to_speak and file_name:
    try:
        # Generate the speech with the selected accent
        tts = gTTS(text=text_to_speak, lang='en', slow=False, tld=selected_tld)

        # Save the speech to an MP3 file
        file_path = os.path.join(output_dir, f"{file_name}.mp3")
        tts.save(file_path)

        print(f"\nSuccessfully generated sound file at {file_path}")
        print(f"Used accent: {accent_profiles.get(choice, {'name': 'US English (default)'})['name']}")
    except Exception as e:
        print(f"\nFailed to generate sound file: {e}")
else:
    print("\nPlease provide both a phrase and a file name.")
