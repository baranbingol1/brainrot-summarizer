from utils import *
from prompts import *

from langchain.chains.summarize import load_summarize_chain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_env()

model_name = "gpt-4o-mini"

llm = ChatOpenAI(
    model=model_name,
    temperature=0.7,
    max_tokens=4096,
    max_retries=2
)

stuff_chain = load_summarize_chain(llm, chain_type="stuff")
map_reduce_chain = load_summarize_chain(llm, chain_type="map_reduce")

def process_document(file_path):

    documents = load_document(file_path)

    full_text = " ".join(doc.page_content for doc in documents)

    token_count = get_token_count(model_name, full_text)
    # print("Total token count is:", token_count)
    if token_count <= 120000:
        summary = stuff_chain.run(documents)
    else:
        summary = map_reduce_chain.run(documents)

    brainrot_prompt = PromptTemplate.from_template(brainrot_template)
    formatted_prompt = brainrot_prompt.format(content=summary)

    return llm.invoke(formatted_prompt).content

if __name__ == "__main__": # for testing
    print(process_document("1-s2.0-S0950705124003721-main-2.pdf"))