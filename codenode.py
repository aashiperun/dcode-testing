from datetime import datetime
from pathlib import Path
from .node import Node
import openai
import os

class CodeNode(Node):
    """ 
    Extends the Node class. Use this for code files
    """
    def store_file_as_txt(self):
        """
        Converts file contents into a string and stores it
        """
        try:
            self.content = Path(self.path).read_text()
        except:
            print("Cannot read file")

    def generate_description(self):
        """
        Generates a description of a code file and stores it
        """
        if self.content == '':
            return
        openai.api_key = os.getenv("OPENAI_API_KEY")
        chatgpt = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
                {"role": "system", "content": "You are a software engineering assistant. Summarize this code file in 2 lines or less."},
                {"role": "user", "content": self.content}
            ]
        )
        self.description = chatgpt["choices"][0]["message"]["content"]
        self.updated_time = datetime.now()