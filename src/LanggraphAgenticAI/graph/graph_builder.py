from langgraph.graph import StateGraph
from ..State.state import State
from langgraph.graph import START,END
from ..Nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def basicchatbot_graph(self):
        """
        Building a basic chatbot graph using Langggraph
        This method will be used to build the graph for the basic chatbot and
        integrates it into the graph. The chatbot node is set as both the entry and exit point of the 
        graph.
        """

        self.basic_chatbot_node=BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self, usecase):
        """
        Sets up and compiles the graph based on the selected use case.
        
        Args:
            usecase (str): The selected use case for the graph
            
        Returns:
            CompiledGraph: The compiled LangGraph graph ready for execution
        """
        
        # Map use cases to their respective graph building methods
        usecase_mapping = {
            "Basic Chatbot": self.basicchatbot_graph,
            # Add more use cases here as you expand the application
            # "Advanced Chatbot": self.advanced_chatbot_graph,
            # "RAG Chatbot": self.rag_chatbot_graph,
        }
        
        # Check if the use case is supported
        if usecase not in usecase_mapping:
            raise ValueError(f"Unsupported use case: {usecase}. Available options: {list(usecase_mapping.keys())}")
        
        # Build the graph for the selected use case
        graph_method = usecase_mapping[usecase]
        graph_method()
        
        # Compile and return the graph
        compiled_graph = self.graph_builder.compile()
        return compiled_graph