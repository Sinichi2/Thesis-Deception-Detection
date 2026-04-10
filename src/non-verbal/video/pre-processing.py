import mediapipe as mp
import numpy as np
from loader import loader_many




def mediapipe():
    '''
        This will be for face_detection 
        videos -> Loaded videos 
    '''
    TRUTH_DIR = os.path.expanduser("../dataset/RealLifeDeceptionDetection/Clips/Truthful")
    DECEPTIVE_DIR = os.path.expanduser("../dataset/RealLifeDeceptionDetection/Clips/Deceptive")

    videos, labels = loader_many([TRUTH_DIR, DECEPTIVE_DIR], target_size=(128,128), max_frames=30)
    