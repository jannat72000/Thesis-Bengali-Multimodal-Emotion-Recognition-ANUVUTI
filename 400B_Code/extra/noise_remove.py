import os
from pydub import AudioSegment
from noisereduce import reduce_noise

def remove_background_noise(input_folder, output_folder, noise_profile_folder):
    # Check if the input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
        return

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each audio file in the input folder
    for audio_file in os.listdir(input_folder):
        if audio_file.endswith(".wav"):  # Adjust the file extension as needed
            audio_path = os.path.join(input_folder, audio_file)

            # Generate output path for the processed audio file
            output_path = os.path.join(output_folder, audio_file)

            # Assuming each audio file has a corresponding noise profile file
            noise_profile_file = os.path.join(noise_profile_folder, f"{audio_file.split('.')[0]}_noise_profile.wav")

            if os.path.exists(noise_profile_file):
                print(f"Processing {audio_file}...")
                remove_background_noise_single(audio_path, output_path, noise_profile_file)
                print(f"Processed audio saved to {output_path}")
            else:
                print(f"No noise profile found for {audio_file}. Skipping.")

def remove_background_noise_single(audio_path, output_path, noise_profile_path):
    # Load audio
    audio = AudioSegment.from_file(audio_path)

    # Load the noise profile
    noise_profile = AudioSegment.from_file(noise_profile_path)

    # Reduce noise from the audio with a more aggressive parameter
    reduced_audio = reduce_noise(audio, noise_profile, prop_decrease=1.5)

    # Save the processed audio to the output path
    reduced_audio.export(output_path, format="wav")

# Example usage
input_folder = r"C:\\Users\\ehsan\\Desktop\\noise"
output_folder = r"C:\\Users\\ehsan\\Desktop\\noise_remove"
noise_profile_folder = r"C:\\Users\\ehsan\\Desktop\\rubbish"

remove_background_noise(input_folder, output_folder, noise_profile_folder)
