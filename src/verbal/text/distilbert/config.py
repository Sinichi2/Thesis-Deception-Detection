from dataclasses import dataclass 
# from typing import Protocol
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch 


@dataclass 
class distilBertConfig:
    model_name: str = "distilbert/distilbert-base-uncased"
    model_dtype = torch.bfloat16
    