#LLM & HuggingFace Integration
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


#Tokenizer + model: meta-llama/Meta-Llama-3.1-8B-Instruct
#Generates a JSON-style “plan” that can be sent to frontend.
