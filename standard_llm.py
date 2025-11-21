import os
import warnings
warnings.filterwarnings('ignore')
os.environ['TRANSFORMERS_VERBOSITY'] = 'error'
os.environ['TOKENIZERS_PARALLELISM'] = 'False'

from transformers import AutoModelForCausalLM, AutoTokenizer

class StandardLLM:
    def __init__(self, checkpoint="HuggingFaceTB/SmolLM-135M", device="cpu"):
        self.checkpoint = checkpoint
        self.device = device

        # Generation settings
        self.max_tokens = 100
        self.temperature = 0.5
        self.top_p = 0.99
        self.min_p = 0.2

        # Load model & tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        self.model = AutoModelForCausalLM.from_pretrained(checkpoint).to(self.device)

    def generate_response(self, user_input):
        
        input_tokens = self.tokenizer.encode(user_input, return_tensors="pt").to(self.device)

        
        output = self.model.generate(
            input_tokens,
            max_new_tokens=self.max_tokens,
            temperature=self.temperature,
            top_p=self.top_p,
            min_p=self.min_p,
            do_sample=True
        )

        
        full_text = self.tokenizer.decode(output[0], skip_special_tokens=True)

        # Remove original input from start
        new_text = full_text[len(user_input):]
        return new_text.strip()




