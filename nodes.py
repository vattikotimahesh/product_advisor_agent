from prompts import SYSTEM_PROMPT
from utils import use_gcp
from state import Suggest_state
from langgraph.prebuilt import ToolNode
#tools_condition
from langchain_core.messages import (SystemMessage,
    BaseMessage, 
    HumanMessage, 
    RemoveMessage)
from tools import get_product,get_all_products
SUMMARY_TRIGGER = 12
KEEP_RECENT = 6
use_tools = [get_product,get_all_products]

def model_with_tools(tools):
    #Give LLM access to tools
    
    llm = use_gcp()
    return llm.bind_tools(tools = tools)





def assistant(state:Suggest_state):
    prompt = [SystemMessage(SYSTEM_PROMPT)]
    if summary := state.get("summary"):
        prompt.append(SystemMessage(f"Summary of earlier conversation: {summary}"))
    response = model_with_tools(use_tools).invoke(prompt + state["messages"])
    return {"messages": [response]}

    
    #Ask LLM what to do/respond
    # llm_tools = model_with_tools(
    #     tools = use_tools 
    # )
    
    # response = llm_tools.invoke([SystemMessage(SYSTEM_PROMPT)]+ state['messages']# )
    #state['messages'] = [response]
    #return {"messages": [response]}
    
    



def safe(messages: list[BaseMessage], KEEP_RECENT:int) -> int:
    #Find a safe place to split old/new messages
    cut = len(messages) - KEEP_RECENT
    while cut > 0 and not isinstance(messages[cut], HumanMessage):
        cut -= 1
    return max(cut,0)
    #return cut

def conversation(state: Suggest_state):
    #Compress old conversation into a summary
    messages = state['messages']
    cut=safe(messages,KEEP_RECENT)
    #old=cut[:cut]
    old = messages[:cut]
    
    if not old:
        return {}
    
    instruction=(
       "Summarise this part of a product-advice conversation in under 120 words. "
       "Keep the customer's stated concerns and which products were discussed. "
       "Do not invent anything."
    )
    
    previous = state.get("summary")
    if previous:
        instruction = f"Summary so far : {previous}\n\n{instruction} Extend it"
        
    result = use_gcp().invoke([SystemMessage(instruction)] + old)
    return {
        
        'summary':result.content,
        'messages': [RemoveMessage(id=m.id ) for m in old]
        
    }
    
def use_tool_node() -> ToolNode:
    #Execute the tools
    
    """ This method returns the tool node

    Returns:
    
        _type_: _description_
        
    """
    return ToolNode(tools = use_tools)

def customer_info(state:Suggest_state):#Extract/store customer details
    return state
    