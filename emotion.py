
from deepface import DeepFace

from image import label_image


file_path = '/Microexpressions/faces/multi_face.jpg'


emotion_list = DeepFace.analyze(
    img_path    = file_path,
    actions     = ['emotion']
)

# results = list of dicts
# [{'emotion': {'angry': 1.220522923180145e-10, 'disgust': 1.9222593053648094e-17, 'fear': 1.4587384577179063e-11, 'happy': 99.93095397949219, 'sad': 3.6937935349312667e-09, 'surprise': 2.203453218496687e-09, 'neutral': 0.06904496112838387}, 'dominant_emotion': 'happy', 'region': {'x': 653, 'y': 604, 'w': 163, 'h': 163}, 'face_confidence': 9.231560152140446}]

print("Detected {} faces".format(len(emotion_list)))
label_image(file_path, emotion_list)
print("Done")

