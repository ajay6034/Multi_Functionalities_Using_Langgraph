

## 🔄 Multi-Functional AI Workflow using LangGraph and LLaMA 3

This project demonstrates a simple yet powerful **LangGraph-based workflow** using **LangChain + Groq’s LLaMA 3.1 8B Instant model** to process and transform AI-related input queries in a multi-step pipeline.

### 🚀 Project Overview

The goal of this project is to build a **modular AI reasoning flow** using the [LangGraph](https://docs.langchain.com/langgraph) framework. It showcases how different tasks like text generation, transformation, and workflow control can be composed using graph-based logic.

---

### 🧠 Key Features

* **Graph-based workflow:** Implements a directed workflow graph where each node performs a specific function.
* **Integration with LLaMA 3.1 via Groq:** Utilizes the ultra-fast inference capability of `ChatGroq`.
* **Extensible architecture:** Easy to add or modify new functional nodes.

---


### ⚙️ Workflow Explanation

The workflow consists of the following two function nodes:

1. **`function1`: LLM-based response generation**

   * Uses the `ChatGroq` interface with LLaMA 3.1.
   * Generates a response for the query: `"Tell me about current trends in AI"`.
   * Acts as the entry point of the graph.

2. **`function2`: Post-processing**

   * Takes the output from `function1` and converts it to uppercase.
   * Acts as the final node (finish point) of the graph.

#### 🧩 Workflow Structure:

![output](https://github.com/user-attachments/assets/0b00ee28-16d9-4428-9e8a-fcd52aaabd85)


### 📸 Visualization

The workflow graph is rendered using Mermaid diagram, and optionally displays a PNG using:

```python
display(Image(app.get_graph(xray=True).draw_mermaid_png()))
```

Mermaid syntax can also be printed for debugging:

```python
print(app.get_graph().draw_mermaid())
```


