from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()  # Loads .env file

llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), temperature=0)
prompt = PromptTemplate.from_template("Break down the following task into subtasks: {input}")
plan_agent = LLMChain(llm=llm, prompt=prompt)

def get_subtasks(input):
    return plan_agent.run(input) 