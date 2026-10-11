from utils.model_loader import Model_Loader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition

from tools.weather_info import WeatherInfoTool
from tools.place_search import PlaceSearchTool
from tools.expense_calculator import ExpenseCalculatorTool
from currency_conversion_tool import CurrencyConversionTool





class GraphBuilder():
    def __init__(self):
        pass


    def agent_function(self, state: MessagesState):
         """Main agent function"""
        user_question = state["messages"]
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {"messages": [response]}


    def build_graph(self):
       graph_builder = StateGraph(MessagesState)
       graph_builder.add_node("agent", self.agent_function)
       graph_builder.add_node("weather_info", ToolNode(WeatherInfoTool()))
       graph_builder.add_edge(START, "agent")
       graph_builder.add_conditional_edges("agent", tools_condition)
       graph_builder.add_edge("tools", "agent")
       graph_builder.add_edge("agent", END)
       self.graph = graph_builder.compile()

       return self.graph
