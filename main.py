import openai
import numpy as np
from generate_paper import LLM_paper

generator_X = np.array([
    'Write a systematic survey or overview about the effectiveness of various scaffold cue presentation and methods to combine gradient approaches in neural tissue engineering for directed cell migration, with a focus on chemical, adhesive, mechanical, topographical, and electrical types of gradients.',
    "Write a systematic survey or overview about the theological and philosophical implications of Thomas Aquinas' analysis of the effects of Original Sin, as presented in his work Summa Theologica.",
    'Write a systematic survey or overview about the impact of political partisanship on COVID-19 vaccination rates and attitudes in the United States, including an analysis of how party affiliation influences beliefs in vaccine conspiracy theories, trust in government and science, and overall concern over the virus.'
])

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

generator_Y_hat = myModel.generate_papers(generator_X, instructions)
print('paper')
print(generator_Y_hat)