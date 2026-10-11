# Product Advisor Agent

A conversational AI agent built with **LangGraph** and **Google Gemini (Flash-Lite)** that helps customers find the right products from the LReal catalog. The agent understands a customer's needs (skin type, problem, budget) and recommends suitable products using tool calling.

## Features

- **Tool-calling agent**: the assistant decides when to look up product data and calls tools to fetch it.
- **Product catalog tools**: `get_all_products` returns the full catalog; `get_product(product_id)` returns one product's details.
- **Conditional routing**: the graph routes between the assistant, the tools, and a summarization step.
- **Conversation summarization**: once a conversation grows past a set number of messages, it is summarized to keep context short.
- **LangGraph Studio ready**: includes a `langgraph.json` config so the graph can be run and inspected with the LangGraph dev server.

## How It Works

```
START -> assistant --(tool call?)--> tools -> assistant
                  \--(long chat?)--> summarize -> END
                  \--(otherwise)---> END
```

1. The user sends a message.
2. The `assistant` node (Gemini) decides whether it needs product data.
3. If so, the `tools` node runs a catalog lookup and returns the result to the assistant.
4. The assistant replies with a recommendation.
5. If the conversation exceeds the message threshold, the `summarize` node condenses the history.

## Project Structure

| File | Purpose |
|---|---|
| `graph.py` | Builds the LangGraph `StateGraph` and its routing logic |
| `nodes.py` | Node functions (assistant, tools, summarization) |
| `state.py` | Graph state definition |
| `tools.py` | Catalog tools (`get_all_products`, `get_product`) |
| `prompts.py` | System prompts for the agent |
| `utils.py` | Helper functions |
| `main.py` | Entry point to run the agent |
| `data/p.json` | Product catalog (id, category, name, description, price in INR, size, usage, benefits, problems solved, suitable for) |
| `langgraph.json` | LangGraph dev server configuration |

## Tech Stack

- Python
- LangGraph, LangChain
- Google Gemini (Flash-Lite)
- `uv` for dependency management

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/vattikotimahesh/product_advisor_agent.git
   cd product_advisor_agent
   ```

2. **Install dependencies** (uses `uv`)
   ```bash
   uv sync
   ```

3. **Add your API key**: create a `.env` file in the project root:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
   Never commit this file. It is listed in `.gitignore`.

4. **Run the agent**
   ```bash
   uv run main.py
   ```
   Or run it in LangGraph Studio:
   ```bash
   uv run langgraph dev
   ```

## Example Conversation

```
User:  I have dry skin and need a gentle face cleanser under ₹400.
Agent: [calls get_all_products]
       I'd recommend the HydraGlow Gentle Face Cleanser (₹349, 100 ml). It is
       hydrating, suited for dry and combination skin, and cleanses without
       stripping moisture. Wet your face, apply a small amount, massage, and rinse.
```

*(Replace with a real output from your agent.)*

## Future Improvements

- Replace the full-catalog lookup with semantic search using embeddings and a vector database
- Add customer profile memory across sessions
- Add a simple web UI
- Add automated tests for the tools and routing

## Author

**Mahesh Vattikoti**
[LinkedIn](https://linkedin.com/in/vattikotimahesh) | vattikotimahesh56@gmail.com
