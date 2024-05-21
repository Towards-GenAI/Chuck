##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Chuck [Towards-GenAI] (https://github.com/Towards-GenAI)
##################################################################################################
#Importing dependencies
import chainlit as cl

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig
##################################################################################################
#Defining the class
@cl.on_chat_start
async def on_chat_start():
    
    #send imgae with file path
    elements=[
        cl.Image(name="logo", display="inline",path="tushar.png")
    ]
    
    #await
    await cl.Message(content="Hello! I'm Chuck. How can I help you?",elements=elements).send()

    
    model=ChatGroq(temperature=0.5, model="llama3-70b-8192")
    
    #system Prompt
    
    prompt= ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are expert in Data Scinece and updated in all latest developments"
                
            ),
            ("human", "{question}"),
    ])
    
    
    #runnable Cl chains
    runnable=prompt | model |StrOutputParser()
    cl.user_session.set("runnable",runnable)
    
    
    
#On Message
@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()
    
##################################################################################################