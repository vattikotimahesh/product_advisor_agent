from graph import create_graph
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import HumanMessage


def main():
    graph = create_graph().compile(checkpointer=InMemorySaver())
    cfg = {"configurable": {"thread_id": "cli-session"}}
    print("Product advisor ready. Type 'exit' to quit.")
    while True:
        try:
            text = input("You: ")
        except:
            (KeyboardInterrupt, EOFError):
            print("\nended")
            break

        if text.strip().lower() in {"exit", "quit", ""}:
            break
        
        out = graph.invoke({"messages": [HumanMessage(text)]}, cfg)
        print("Advisor:", out["messages"][-1].text, "\n")


if __name__ == "__main__":
    main()


#test.py → main.py → graph.py → nodes.py → tools.py → utils.py.