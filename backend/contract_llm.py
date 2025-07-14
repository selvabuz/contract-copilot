from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI

prompt = PromptTemplate(
    input_variables=["chunk"],
    template="Extract key clauses and score risk for this contract section: {chunk}"
)
llm = ChatOpenAI(model_name="gpt-3.5-turbo")  # Replace with your preferred LLM
chain = LLMChain(llm=llm, prompt=prompt)

def analyze_chunks(chunks):
    return [chain.run(chunk=ch) for ch in chunks]