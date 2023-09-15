import numpy as np
from .prompt_engineering import generate_iterations

class LLM_paper():
    def __init__(self, llm_model="gpt-3.5-turbo", iterations=1, max_total_time=3600):
        self.llm_model = llm_model
        self.iterations = iterations
        self.timeout = max_total_time

    def generate_papers(self, generator_X, instructions):
        paper_list = []
        for ask_q in generator_X:
            try:
                this_paper = generate_iterations(
                    ask_q,
                    instructions,
                    self.llm_model,
                    self.iterations,
                )
                paper_list.append(this_paper)
            except:
                paper_list.append(None)
        return np.array(paper_list)