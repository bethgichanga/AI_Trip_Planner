import datetime
import os
import traceback
from agent.agentic_workflow import GraphBuilder
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.responses import JSONResponse
from utils.save_to_document import save_document

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    question: str


@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    try:
        print(query)
        graph = GraphBuilder(model_provider="groq")
        react_app = graph()

        # Commented out temporarily in case mermaid.ink times out or fails
        # png_graph = react_app.get_graph().draw_mermaid_png()
        # with open("my_graph.png", "wb") as f:
        #     f.write(png_graph)

        messages = {"messages": [query.question]}
        output = react_app.invoke(messages)

        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content
        else:
            final_output = str(output)

        return {"answer": final_output}
    except Exception as e:
        traceback.print_exc()  # Prints the exact error to your terminal
        return JSONResponse(status_code=500, content={"error": str(e)})
