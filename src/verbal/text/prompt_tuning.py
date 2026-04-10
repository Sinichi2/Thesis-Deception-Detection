from peft import PromptTuningConfig, PromptEmbedding
from typing import List



def promptTuning(
    peft_type = "PROMPT_TUNING", 
    task_type = "SEQ_2_SEQ_LM", 
    num_virtual_tokens=20, 
    token_dim=768, 
        ) -> List[str]:
    pass