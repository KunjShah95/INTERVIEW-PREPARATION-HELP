from langchain.llms import BaseLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from claude_api import get_claude_response
from gemini_api import get_gemini_response

class ClaudeAI(BaseLLM):
    def _call(self, prompt: str) -> str:
        return get_claude_response(prompt)

class GeminiAI(BaseLLM):
    def _call(self, prompt: str) -> str:
        return get_gemini_response(prompt)

# Define the prompt template
prompt_template = """Answer the following interview question in a detailed and professional manner:
{question}"""

prompt = PromptTemplate(input_variables=["question"], template=prompt_template)

# Define which LLM to use (Claude or Gemini)
def choose_llm(model: str) -> BaseLLM:
    if model == "claude":
        return ClaudeAI()
    elif model == "gemini":
        return GeminiAI()
    else:
        raise ValueError("Invalid model choice. Choose either 'claude' or 'gemini'.")

# Set up Langchain chain
def generate_answer_with_langchain(question: str, model: str = "claude") -> str:
    """Generate interview preparation answers using Claude or Gemini AI."""
    llm = choose_llm(model)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(question)
