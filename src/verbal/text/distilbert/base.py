from transformers import pipeline, DistilBertTokenizer, TFDDistilBertModel

import torch 

classifier = pipeline(
    task = "text-classification", 
    model = "distilbert/distilbert-base-uncased",
    dtype = torch.bfloat16,
    device = 0 # 
)