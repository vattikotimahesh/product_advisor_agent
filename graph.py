from langgraph.graph import START,END,StateGraph
from nodes import assistant, use_tool_node,conversation,SUMMARY_TRIGGER
from state import Suggest_state

from  langgraph.prebuilt import tools_condition


def should_summarize(state:Suggest_state) -> str:
    if len(state['messages']) > SUMMARY_TRIGGER:
        return 'summarize'
    return END

def after_assistant(state:Suggest_state)-> str:
    last=state['messages'][-1]
    if getattr(last, "tool_calls", None):
        return "tools"
    return should_summarize(state)
    
    

def create_graph()-> StateGraph:
    '''
    This method creats a graph
    
    '''
    my_graph = StateGraph(Suggest_state)
    
    my_graph.add_node('assistant',assistant)
    my_graph.add_node('tools',use_tool_node())
    my_graph.add_node("summarize",conversation)
    #my_graph.add_node('cust_info',customer_info)
    
    
    # to do need define right edges
    
    my_graph.add_edge(START,'assistant')
    
    my_graph.add_conditional_edges(
        'assistant',
        after_assistant,        
        {
            'tools': 'tools',
            'summarize': 'summarize',
            END: END,
        },
    )
    my_graph.add_edge('tools',
                    'assistant')
    my_graph.add_edge("summarize", END)
    # my_graph.add_edge('assistant','cust_info')
    
    # my_graph.add_edge('cust_info',END)
    
    return my_graph