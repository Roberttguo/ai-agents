import os

api_key_openai = os.getenv("OPENAI_API_KEY")
api_key_perplexity = os.getenv("PERPLEXITY_API_KEY")
api_key_gemini = os.getenv("GEMINI_API_KEY")

input_loc=os.getenv("INPUT_LOC", default="local")