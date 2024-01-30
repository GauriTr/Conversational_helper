from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

from langchain_community.chat_models import ChatOpenAI

import os


from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)

from langchain.schema import SystemMessage



openai_api_key = os.environ.get('OPENAI_API_KEY')

chatllm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.9, model='gpt-3.5-turbo-1106')

sys_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content="You are a conversational helper, you often give witty, smart, and sarcastic replies in a polite and professional tone in the user's language to {conversational_text}. Always give a list of possible replies as a human."
        ),  
        MessagesPlaceholder(
            variable_name="chat_history"
        ),  
        HumanMessagePromptTemplate.from_template(
            "{conversational_text}"
        ),  
    ]
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

chat_llm_chain = LLMChain(
    llm=chatllm,
    prompt=sys_prompt,
    verbose=True,
    memory=memory,
)

def get_langchain_response(input_text):
    return chat_llm_chain.run(input_text)

