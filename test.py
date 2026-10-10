from main import graph
from state import Suggest_state
from langchain_core.messages import HumanMessage


result=graph.invoke(Suggest_state(
    messages = [
        HumanMessage(content = 'i need a fix oil and dry skin')
        ]
    )
)
print(result)