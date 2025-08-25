import json
import os
import openai
from perplexipy import PerplexityClient
from common import constant
from utils import https_client_input

@slf4j
class AIAgent:
    def __init__(self, ai_name):
        self.ai_name=ai_name
        self.client = None
        self._init_client()


    def _init_client(self):
        if self.ai_name == "openai":
            if not api_key_openai:
                raise Exception("No api key for "+self.ai_name)
            self.client=openai.OpenAI(api_key=api_key_openai)
        if self.ai_name == "Perplexityai":
            if not api_key_perplexity:
                raise Exception("No api key for "+self.ai_name)
            self.client=PerplexityClient(api_key=api_key_perplexity)
        self.log.info("initialization complete!")

    def ask_question(self, prompt:str):
        if input_loc == "local":
            question = input(prompt)
        else:
            question = submit()
        return question

    def query_ai(self):
        content=self.askquestion("Ask your question...")
        if self.ai_name == "openai":
            response = client.chat.completions.create(
                model="sonar-small-online", #"gpt-4-1106-preview",
                messages=[{"role":"user","content":content}],
                #tools=available_tools,
                #tool_choice="auto",  # This allows the model to decide whether to call a tool
            )
            self.log.info("AI returned: " +response)
            return

        if self.ai_name == "Perplexityai":
            pass