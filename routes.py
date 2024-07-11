from flask import request, jsonify
from ai_handler import AIHandler
from utils import preprocessing_text, random_sequence

ai_handler = AIHandler()

def setup_routes(app):
    @app.route('/singleLanguageAssessmentSuggetion/<string:name>/<string:skills>/<string:marks>/<string:totalmarks>/', methods=['GET'])
    def generate_content(name, skills, marks, totalmarks):
        # print(name, skills, marks, totalmarks)
        skills_list = [str(skill) for skill in skills.split(',')]
        marks_list = [int(mark) for mark in marks.split(',')]
        total_marks_list = [int(totalmark) for totalmark in totalmarks.split(',')]
        # print(skills_list, marks_list, total_marks_list)
        greeting_ = f"give me a greeting to tell to the candidate like hi {name}, I hope you are well like that within one line"
        tipsForDevelopingYourSkills_ = f"give me some tips to develop skills on {skills} within three lines"
        ideaForFurtherProject_ = f"give me some idea to do one project with {skills} skills, like you can do this project to enhance your skill like that format (just suggestible format) within one line"
        futureScope_ = f"give me some future scope with {skills} skills within one line, like {name} you have these future scopes like that"
        linksForFurtherLearning_ = f'give some official link for this {skills} skills to enhance {name} skills, give me just one valid link per skill, you have to return in dictionary format like "python":"link"'

        greeting = preprocessing_text(ai_handler.promt(greeting_, name, skills_list, marks_list, total_marks_list))
        tipsForDevelopingYourSkills = preprocessing_text(ai_handler.promt(tipsForDevelopingYourSkills_, name, skills_list, marks_list, total_marks_list))
        ideaForFurtherProject = preprocessing_text(ai_handler.promt(ideaForFurtherProject_, name, skills_list, marks_list, total_marks_list))
        futureScope = preprocessing_text(ai_handler.promt(futureScope_, name, skills_list, marks_list, total_marks_list))

        suggested_links = random_sequence(skills_list, 1)

        suggestion = {
            "greeting": greeting,
            "tipsForDevelopingYourSkills": tipsForDevelopingYourSkills,
            "ideaForFurtherProject": ideaForFurtherProject,
            "futureScope": futureScope,
            "linksForFurtherLearning": suggested_links
        }
        print(suggestion,type(suggestion))
        return jsonify(suggestion)
