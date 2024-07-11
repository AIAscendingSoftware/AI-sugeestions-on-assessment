import re
import random

def remove_stars(text, remove_from_edges=False):
    output_string = text.replace("*", "").replace("#", "").replace("+\n","").replace(" \n","").replace("    ","").replace("\\n","")
    
    if remove_from_edges:
        while output_string and (output_string[0] == "*" or output_string[0] == "#"):
            output_string = output_string[1:]
        while output_string and (output_string[-1] == "*" or output_string[-1] == "#"):
            output_string = output_string[:-1]

    return output_string

def preprocessing_text(generated_text):
    pattern = r"(?<!\\)\n|\t|\+|-|\r"  # Matches any of the special characters except escaped ones
    json_string = re.sub(pattern, "", generated_text)
    output_text = remove_stars(json_string, remove_from_edges=True)
    return output_text

def random_sequence(values_list, num_urls):
    resources = {
        "ANGULAR": ["https://v17.angular.io/docs", "https://egghead.io/", "https://www.udemy.com/course/mastering-angular-interview-questions-e-commerce-project/?couponCode=ST9MT71624"],
        "CSS": ["https://www.w3schools.com/css/", "https://www.codecademy.com/learn/learn-css", "https://www.coursera.org/learn/introcss"],
        "HTML": ["https://developer.mozilla.org/en-US/docs/Learn/HTML", "https://www.w3schools.com/html/", "https://www.codecademy.com/learn/learn-html"],
        "REACT": ["https://react.dev/learn/tutorial-tic-tac-toe", "https://www.udemy.com/course/react-the-complete-guide-incl-redux/?couponCode=ST9MT71624", "https://www.coursera.org/search?query=react%20js"],
        "JAVA": ["https://docs.oracle.com/javase/tutorial/", "https://www.udacity.com/course/java-programming-nanodegree--nd079", "https://www.coursera.org/specializations/java-programming"],
        "PYTHON": ["https://docs.python.org/3/tutorial/", "https://www.codecademy.com/learn/learn-python", "https://www.udacity.com/course/advanced-python-techniques--cd0010"],
        "CSHARP": ["https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/", "https://www.udemy.com/course/complete-csharp-masterclass/?couponCode=ST9MT71624", "https://www.coursera.org/specializations/programming-unity-game-development"],
        "NODEJS": ["https://nodejs.org/docs/latest/api/", "https://www.codecademy.com/learn/learn-node-js", "https://www.udemy.com/course/nodejs-the-complete-guide/?couponCode=ST9MT71624"],
        "JAVASCRIPT": ["https://developer.mozilla.org/en-US/docs/Web/JavaScript", "https://www.codecademy.com/learn/introduction-to-javascript", "https://www.udacity.com/course/full-stack-javascript-developer-nanodegree--nd0067"],
        "AWS": ["https://aws.amazon.com/training/", "https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/?couponCode=ST9MT71624", "https://learn.microsoft.com/en-us/training/"],
        "MICROSOFTAZURE": ["https://www.coursera.org/learn/microsoft-azure-cloud-services", "https://www.udemy.com/courses/search/?q=microsoft+azure&src=sac&kw=micros", "https://www.udemy.com/courses/search/?q=microsoft+azure&src=sac&kw=Microsoft+Az"],
        "MATLAB": ["https://www.mathworks.com/help/matlab/learn-matlab.html", "https://www.coursera.org/search?query=MATLAB", "https://www.udacity.com/catalog/all/any-price/any-school/any-skill/any-difficulty/any-duration/any-type/relevance/page-1?searchValue=MATLAB"],
        "R": ["https://www.r-project.org/", "https://www.coursera.org/learn/r-programming", "https://www.datacamp.com/courses/intro-to-r"],
        "KOTLIN": ["https://kotlinlang.org/docs/home.html", "https://www.coursera.org/search?query=Kotlin", "https://www.udacity.com/catalog/all/any-price/any-school/any-skill/any-difficulty/any-duration/any-type/relevance/page-1?searchValue=kotline"],
        "SWIFT": ["https://developer.apple.com/swift/", "https://www.codecademy.com/learn/learn-swift", "https://www.coursera.org/search?query=swift"],
        "PHP": ["https://www.php.net/manual/en/", "https://www.w3schools.com/php/", "https://www.codecademy.com/learn/paths/php-skill"],
        "FIREBASE": ["https://firebase.google.com/docs/", "https://www.coursera.org/search?query=firebase", "https://www.udacity.com/catalog/all/any-price/any-school/any-skill/any-difficulty/any-duration/any-type/relevance/page-1?searchValue=firebase"]
    }

    suggested_links = {}
    for language in values_list:
        result = language.replace(' ', '')
        lang_key = result.upper()
        if lang_key in resources:
            suggested_links[language] = random.choice(resources[lang_key])
    
    return suggested_links
