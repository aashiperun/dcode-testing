from datetime import datetime
from pathlib import Path
from .node import Node
import openai
import os

class FolderNode(Node):
    """ 
    Extends the Node class. Use this for directories 
    """
    def generate_description(self):
        """
        Generates a description of a directory and stores it
        """
        if len(self.children) == 0: # Empty directory
            return
        
        # Get code summaries from children
        summaries = []
        for child in self.children.values():
            if child is None:
                continue
            summaries.append(child.description)

        if len(summaries) == 0: # Empty 
            return
        
        # Combine file descriptions into one long string
        combined_summaries = '\n'.join(summaries) 

        # Use chatGPT to summarize summaries
        openai.api_key = os.getenv("OPENAI_API_KEY")
        chatgpt = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
                {"role": "system", "content": "You are a software engineering assistant. Each of the following paragraphs describes a code file or a folder, which resides in a parent folder. Summarize the overall function of this parent folder in 2 lines or less."},
                {"role": "user", "content": combined_summaries}
            ]
        )
        self.description = chatgpt["choices"][0]["message"]["content"]
        self.updated_time = datetime.now()