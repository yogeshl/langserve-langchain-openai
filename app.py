from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="API Server",
    version="1.0",
    description="A simple AI API server"
)

model=ChatOpenAI()
prompt1 = ChatPromptTemplate.from_template("Provide an essay about {topic}")
prompt2 = ChatPromptTemplate.from_template("Provide an learning mind map about {topic}")

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|model,
    path="/mindmap"
)


if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=5000)