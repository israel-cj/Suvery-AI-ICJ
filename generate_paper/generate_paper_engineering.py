from .prompt_engineering import generate_iterations

class LLM_paper():
    def __init__(self, llm_model="gpt-3.5-turbo", iterations=1, max_total_time=3600):
        self.llm_model = llm_model
        self.iterations = iterations
        self.timeout = max_total_time

    def generate_papers(self, generator_X, instructions):
        paper = generate_iterations(
            generator_X,
            instructions,
            self.llm_model,
            self.iterations,
        )
        return paper