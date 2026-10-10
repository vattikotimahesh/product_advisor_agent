from langchain.chat_models import BaseChatModel,init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()


def use_model(model:str,**args:dict)->BaseChatModel:
    
    return init_chat_model(
        model = model,
        **args
    )
    
def use_gcp()->ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model='gemini-3.5-flash-lite',
        project=os.getenv('PROJECT_ID')
    )
    
    
    
if __name__ == "__main__":
    
    
    llm = use_model(model = os.getenv ('MODEL_NAME','gemini-3.5-flash-lite'),
                  model_provider = "google_genai",
                  project = os.getenv('PROJECT_ID') )
    
    result = llm.invoke('what is the capital of india ?')
    result.pretty_print()
    
    
