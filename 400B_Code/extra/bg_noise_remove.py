import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from noisereduce import reduce_noise

def remove_background_noise(input_folder, output_folder, noise_profile_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each video file in the input folder
    for video_file in os.listdir(input_folder):
        if video_file.endswith(".mp4"):  # Adjust the file extension as needed
            video_path = os.path.join(input_folder, video_file)

            # Generate output path for the processed video
            output_path = os.path.join(output_folder, video_file)

            # Assuming each video has a corresponding noise profile file
            noise_profile_file = os.path.join(noise_profile_folder, f"{video_file.split('.')[0]}_noise_profile.wav")

            if os.path.exists(noise_profile_file):
                print(f"Processing {video_file}...")
                remove_background_noise_single(video_path, output_path, noise_profile_file)
                print(f"Processed video saved to {output_path}")
            else:
                print(f"No noise profile found for {video_file}. Skipping.")

def remove_background_noise_single(video_path, output_path, noise_profile_path):
    video_clip = VideoFileClip(video_path)
    audio = video_clip.audio

    # Save the audio as a temporary file
    temp_audio_path = "temp_audio.wav"
    audio.write_audiofile(temp_audio_path, codec='pcm_s16le')

    # Load the noise profile
    noise_clip = AudioSegment.from_file(noise_profile_path)

    # Reduce noise from the audio
    reduced_audio = reduce_noise(audio_path=temp_audio_path, noise_profile=noise_clip)

    # Replace the original audio in the video clip with the reduced audio
    video_clip = video_clip.set_audio(reduced_audio)

    # Write the processed video to the output path
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

    # Cleanup temporary files
    os.remove(temp_audio_path)

# Example usage
input_folder = r"C:\Users\ehsan\Desktop\edit"
output_folder = r"C:\Users\ehsan\Desktop\Pre_pocessed_Dataset"
noise_profile_folder = r"C:\Users\ehsan\Desktop\noise"

remove_background_noise(input_folder, output_folder, noise_profile_folder)
