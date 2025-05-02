from langgraph.graph import Graph

from langchain_groq import ChatGroq
llm = ChatGroq(model="llama-3.1-8b-instant")
llm.invoke("Hi, how are you?").content

def function1(input):
    llm = ChatGroq(model="llama-3.1-8b-instant")
    response = llm.invoke("Tell me about current trends in AI").content
    return response
function1("Hi")

def function2(input):
    func1_output = input.upper()
    return func1_output
workflow = Graph()
workflow.add_node("function1",function1)
workflow.add_node("function2",function2)
workflow.add_edge("function1","function2")

workflow.set_entry_point("function1")
workflow.set_finish_point("function2")
app = workflow.compile()

from IPython.display import Image, display

# Try simplified (xray) view first
try:
    display(Image(app.get_graph(xray=True).draw_mermaid_png()))
except Exception as e:
    print(e)

# Alternatively, print Mermaid text to debug
print(app.get_graph().draw_mermaid())

app.invoke("Hi, can you give me about ML")
