import google.generativeai as genai
from config import Config

class AIHandler:
    def __init__(self):
        genai.configure(api_key=Config.API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')

    def generate_content(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text

    def promt(self, question, name, skills_list, marks_list, total_marks_list):
        details = ", ".join([f"{marks_list[i]} out of {total_marks_list[i]} in {skills_list[i]}" for i in range(len(skills_list))])
        promt_as_question = f"We have conducted an exam for {name}. The candidate scored {details}, and {name} overall mark is {sum(marks_list)} out of {sum(total_marks_list)} The candidate has written tests for {', '.join(skills_list)}, so {question}."
        return self.generate_content(promt_as_question)
