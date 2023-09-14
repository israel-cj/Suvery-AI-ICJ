import openai
from generate_paper import LLM_paper


sentence = "Write a systematic survey or overview about the effectiveness of incorporating discrete mathematics as a precursor to programming courses in high school and college"
instructions = """
- Synthesize, summarize and analyze old, as well as recent studies, always citing your sources.
- Be mindful of not plagiarizing: when you refer to a paper, you shouldn't just summarize it, you should critically analyze it and discuss all aspects of the paper. 
- Ensure that you are addressing various research questions and make interesting new contributions to the existing field of study. 
- Use different points of view so that you can compare and contrast relevant data and information.
- During the discussion, analyze the entire topic and not only one aspect of it.
- The output must be exclusively in this JSON format: [{"heading":"...", "text" : "..."},{"heading":"...", "text" : "..."},...]
"""
openai.api_key = ""
myModel = LLM_paper(
    llm_model="gpt-3.5-turbo",
    iterations=1,
    max_total_time=3600
)

generator_Y_hat = myModel.generate_papers(sentence, instructions)
print('paper')
print(generator_Y_hat)