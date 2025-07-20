from configparser import ConfigParser
import os

class Config:
    def __init__(self, config_file=None):
        self.config = ConfigParser()
        if config_file is None:
            # Get the directory of this file and construct the path to the config file
            current_dir = os.path.dirname(__file__)
            config_file = os.path.join(current_dir, "uiconfigfile.ini")
        self.config.read(config_file)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(",")
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(",")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(",")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")


