from dotenv import load_dotenv, find_dotenv 
from pathlib import Path
import os

load_dotenv(find_dotenv(".env.text.dev"))


class Config:
    #Dataset declaration
    TRUTH_DIR=os.path.expanduser("../dataset/RealLifeDeceptionDetection/Clips/Truthful")
    DECEPTIVE_DIR=os.path.expanduser("../dataset/RealLifeDeceptionDetection/Clips/Deceptive")

