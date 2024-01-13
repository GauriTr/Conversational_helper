

from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain import PromptTemplate
import os

openai_api_key = os.environ.get('OPENAI_API_KEY')
chatllm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.9, model='gpt-3.5-turbo-1106')

sys_prompt = PromptTemplate(
    input_variables=["conversational_text"],
    template="""You are a conversational helper, you often give witty, smart, and sarcastic replies in a polite and professional tone in the user's language to {conversational_text}. Give a list of possible replies as a human."""
)

system_message_prompt = SystemMessagePromptTemplate(prompt=sys_prompt)

student_prompt = PromptTemplate(
    input_variables=["conversational_text"],
    template="Answer to {conversational_text}"
)
student_message_prompt = HumanMessagePromptTemplate(prompt=student_prompt)

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, student_message_prompt])

chain = LLMChain(llm=chatllm, prompt=chat_prompt)

def get_langchain_response(input_text):
    output = list(chain.invoke(input=input_text).values())
    return "\n".join([str(i) for i in sorted(set(output))])
