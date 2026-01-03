from transformers import pipeline 
import torch 

# 
classifier = pipeline(
    task = "text-classification". 
    model="distilbert-base-uncased-finetuned-sst-2-english",
    dtype = torch.bfloat16
    device = 0 # 
)