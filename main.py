##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Chuck [Towards-GenAI] (https://github.com/Towards-GenAI)
#Importing dependencies
import chainlit as cl

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig

#Defining the class
@cl.on_chat_start
async def on_chat_start():
    
    #send imgae with file path
    elements=[
        cl.Image(name="logo", display="inline",path="tushar.png")
    ]
