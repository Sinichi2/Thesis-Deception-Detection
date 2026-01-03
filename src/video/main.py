import os
import pathlib as path
from loader import loader_many
# from dotenv import load_dotenv

# load_dotenv(TRUTH_DIR, DECEPTIVE_DIR)
TRUTH_DIR = os.path.expanduser("../dataset/RealLifeDeceptionDetection/Clips/Truthful")
DECEPTIVE_DIR = os.path.expanduser("../dataset/RealLifeDeceptionDetection/Clips/Deceptive")

videos, labels = loader_many([TRUTH_DIR, DECEPTIVE_DIR], target_size=(128,128), max_frames=30)

