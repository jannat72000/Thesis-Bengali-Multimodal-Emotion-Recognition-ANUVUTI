# ANUVUTI: A Video Dataset for Emotion Recognition in Bangla

## 📌 Overview
ANUVUTI is a multimodal video dataset developed for emotion recognition in the Bangla language, addressing the scarcity of resources for low-resource languages in affective computing and human-computer interaction research.

The dataset contains **1,035 video clips** capturing seven emotional states expressed by non-professional actors, ensuring realistic and natural emotional expressions.

---

## 🎯 Key Features
- 7 emotion categories: Happiness, Sadness, Anger, Fear, Disgust, Surprise, Neutral  
- Total 1,035 video clips  
- Multimodal dataset (audio + visual)  
- Bangla speech with regional variations  
- Real-world recording environments  
- Resolution: 720p (1280×720) @ 25 FPS  
- Total dataset size: ~497 MB  

---

## 📊 Dataset Summary

| Attribute | Description |
|----------|------------|
| Language | Bangla |
| Total Clips | 1,035 |
| Emotion Categories | 7 |
| Actors | 10 (6 Female, 4 Male) |
| Age Range | 18–25 |
| Clip Duration | 1–4 seconds |
| Format | MP4 |
| Resolution | 720p (1280×720) |
| Frame Rate | 25 FPS |
| Sampling Rate | 44.1 kHz |
| Dataset Size | ~497 MB |

---

## 📂 Dataset Structure

The dataset repository is organized into seven folders, each corresponding to one emotion category:

- Happiness  
- Sadness  
- Anger  
- Fear  
- Disgust  
- Surprise  
- Neutral  

### Distribution of Clips
- 6 primary emotions × 150 clips each = 900 clips  
- Neutral emotion = 135 clips  
- **Total = 1,035 clips**

### Calculation
- 5 sentences × 3 repetitions × 10 actors × 6 emotions = 900  
- 5 sentences × 3 repetitions × 9 actors × neutral = 135  

---

📁 Filename Convention
Each video file in the ANUVUTI dataset follows a structured naming format to ensure easy identification and retrieval.
🧾 Format
P_<ActorNumber>_<EmotionCode>_<SentenceNumber>_(<Repetition>).mp4
📌 Example
P_1_A_1_(1).mp4
🔍 Meaning of Example:
P_1 → First actor
A → Angry emotion
1 → First sentence of the Angry category
(1) → First repetition of that sentence

📊 Filename Structure Breakdown
Component	Description
Actor Number	P_1, P_2, P_3, ..., P_10
Emotion State	A = Angry, D = Disgust, F = Fear, H = Happy, N = Neutral, S = Sad, Sur = Surprise
Sentence Number	1, 2, 3, 4, 5, ... up to 35
Repetition	(1), (2), (3) for repeated recordings

---

## 🧠 Experimental Design & Methodology

### Emotion Selection
Seven fundamental emotional states were selected:
- Angry, Disgust, Sad, Happy, Fear, Surprise, Neutral  

These are based on widely accepted psychological theories of basic human emotions.

---

### Script Design
- 35 Bangla sentences (5 per emotion)  
- Designed to align with emotional context  
- Includes natural, easy-to-express phrases for non-professional actors  

Example:  
বাংলা: উফ! কী বাজে দূর্গন্ধ!  
English: What a bad smell!  

---

### Actor Recruitment
- 10 non-professional actors  
- Age range: 18–25  
- Gender distribution: 6 female, 4 male  

Actors were selected to ensure realistic and natural emotional expressions.

---

### Data Collection
- Recorded using smartphones  
- Conducted in real-world environments (including East West University)  
- Each sentence repeated 3 times  

---

### Actor Preparation
- Guided training sessions  
- Trial recordings before final capture  
- Encouraged natural delivery and regional language variation  

---

### Recording Setup
- Comfortable and relaxed environment  
- Multiple takes for complex emotions (e.g., fear, sadness)  
- Flexible speech expression for authenticity  

---

### Data Processing
- Videos trimmed to 1–4 seconds  
- Standardized to 720p resolution  
- Frame rate fixed at 25 FPS  
- Processed using video editing tools  

---

## 🌍 Data Source Location
East West University  
Dhaka, Bangladesh  

---

## 💡 Value of the Dataset

The ANUVUTI dataset provides significant value for:

- Emotion recognition research in low-resource languages  
- Development of emotion-aware AI systems  
- Multimodal machine learning applications  
- Human-computer interaction (HCI)  
- Sentiment and behavioral analysis  

It also enables interdisciplinary research across computer science, linguistics, and psychology.

---

## ⚠️ Limitations

- Limited dataset size (1,035 clips)  
- Narrow age range (18–25)  
- Limited demographic diversity  
- Possible environmental noise in recordings  
- Cultural subjectivity in emotional expression  

Future work may expand dataset diversity and scale.

---

## 🔐 Ethical Considerations

- Informed consent obtained from all participants  
- Participants were aware of dataset usage  
- Privacy and ethical standards were maintained  

---

## 👨‍🔬 Authors

- Dr. Mohammad Manzurul Islam  
- Jannatul Ferdous Salma  
- Nowshin Tabassum  
- Rubiatis Sadia Nera  
- Kazi Ehsanul Haque  

**Corresponding Author:**  
Dr. Mohammad Manzurul Islam  
📧 mohammad.islam@ewubd.edu


