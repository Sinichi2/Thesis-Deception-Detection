from loader import loader
import os



truth_path = os.environ.get("/content/drive/MyDrive/Thesis/Real-Life-Trial-Dataset/RealLifeDeceptionDetection.2016/Real-life_Deception_Detection_2016/Clips/Truthful")
deception_path = os.environ.get("/content/drive/MyDrive/Thesis/Real-Life-Trial-Dataset/RealLifeDeceptionDetection.2016/Real-life_Deception_Detection_2016/Clips/Deceptive")

loader(truth_path, deception_path)



