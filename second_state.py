from typing import TypedDict,Annotated, Optional
from  langchain_core.messages import (
    BaseMessage,
    AIMessage,
    SystemMessage,
    ToolMessage,
    HumanMessage)

from langgraph.graph import add_messages,MessagesState

class MY_state(MessagesState):
    #messages:[list[BaseMessage],add_messages]
    
    product_id: Optional[str]
    mobile_number: Optional[str]
    email: Optional[str]
    customer_name: Optional[str]
    lead_status: Optional[str]
 