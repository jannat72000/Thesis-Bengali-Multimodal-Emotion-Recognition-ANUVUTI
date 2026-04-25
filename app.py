from flask import Flask, request, jsonify, render_template
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
import tensorflow as tf
import os

app = Flask(__name__)

# Load the saved video model
model_path = os.path.join('models', 'late_fusion_video_model.h5')
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")

video_model = load_model(model_path)

def extract_frames(video_path, num_frames=30):
    try:
        cap = cv2.VideoCapture(video_path)
        frames = []
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_interval = max(total_frames // num_frames, 1)

        for i in range(num_frames):
            cap.set(cv2.CAP_PROP_POS_FRAMES, i * frame_interval)
            ret, frame = cap.read()
            if ret:
                frame = cv2.resize(frame, (224, 224))
                frames.append(frame)
            else:
                break

        cap.release()
        if len(frames) == 0:
            raise ValueError("No frames extracted")
        return np.array(frames)
    except Exception as e:
        print(f"Error extracting frames from {video_path}: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file uploaded'}), 400

    video_file = request.files['video']
    video_filename = video_file.filename
    uploads_dir = os.path.join(app.root_path, 'uploads')
    os.makedirs(uploads_dir, exist_ok=True)
    video_path = os.path.join(uploads_dir, video_filename)
    video_file.save(video_path)

    frames = extract_frames(video_path)

    if frames is not None:
        base_model = MobileNetV2(include_top=False, input_shape=(224, 224, 3), weights='imagenet')
        x = base_model.output
        x = tf.keras.layers.GlobalAveragePooling2D()(x)
        video_model_temp = Model(inputs=base_model.input, outputs=x)

        video_features = video_model_temp.predict(frames)
        video_features = video_features.mean(axis=0).reshape(1, -1)

        video_preds = video_model.predict(video_features)

        predicted_class = np.argmax(video_preds, axis=1)
        class_names = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
        predicted_emotion = class_names[predicted_class[0]]

        return jsonify({'predicted_emotion': predicted_emotion})
    else:
        return jsonify({'error': 'Error extracting features from the video'}), 500

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
