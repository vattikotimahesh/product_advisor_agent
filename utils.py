from langchain.chat_models import BaseChatModel,init_chat_model
from functools import lru_cache

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()


def use_model(model:str,**args:dict) -> BaseChatModel:
    
    return init_chat_model(
        model = model,
        **args
    )
@lru_cache(maxsize=1)    
def use_gcp() -> ChatGoogleGenerativeAI:
    project = os.getenv("PROJECT_ID")
    if not project:
        raise ValueError("PROJECT_ID is not set in your .env file")
    
    
    return ChatGoogleGenerativeAI(
        model=os.getenv('MODEL_NAME','gemini-3.5-flash-lite'),
        project=project,)
    
    
    
    
if __name__ == "__main__":
    
    
    llm = use_model(model = os.getenv ('MODEL_NAME','gemini-3.5-flash-lite'),
                  model_provider = "google_genai",
                  project = os.getenv('PROJECT_ID') )
    
    result = llm.invoke('what is the capital of india ?')
    result.pretty_print()
    
    
