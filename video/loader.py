import pathlib as path 
import os, sys
import cv2

truth_path = os.environ.get("/content/drive/MyDrive/Thesis/Real-Life-Trial-Dataset/RealLifeDeceptionDetection.2016/Real-life_Deception_Detection_2016/Clips/Truthful")
deception_path = os.environ.get("/content/drive/MyDrive/Thesis/Real-Life-Trial-Dataset/RealLifeDeceptionDetection.2016/Real-life_Deception_Detection_2016/Clips/Deceptive")


def loader(truth_path: str, deception_path: str) -> str:
  # truth_path = os.environ.get("/content/drive/MyDrive/Thesis/Real-Life-Trial-Dataset/RealLifeDeceptionDetection.2016/Real-life_Deception_Detection_2016/Clips/Truthful")
  # deception_path = os.environ.get("/content/drive/MyDrive/Thesis/Real-Life-Trial-Dataset/RealLifeDeceptionDetection.2016/Real-life_Deception_Detection_2016/Clips/Deceptive")


  if truth_path.exist():
    print(f"Path exists at {truth_path}")
  else: 
    print(f"Path does not exist at {truth_path}")

  if deception_path.exist(): 
    print(f"Path exists at {deception_path}")
  else: 
    print(f"Path does not exist at {deception_path}")


