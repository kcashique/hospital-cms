from werkzeug.wrappers import Response
from jinja2 import Environment, FileSystemLoader


#jinja 2 configurations
environment = Environment(
    loader=FileSystemLoader("modules/templates/"),
    autoescape=True,  # Enable autoescaping for HTML
    trim_blocks=True,  # Trim leading and trailing whitespace from blocks
    lstrip_blocks=True, 
    )


def index(self):
    data = "hello World!"
    return Response(data)


def doctors(self):
    students = [
        {"name": "Sandrine", "score": 100},
        {"name": "Gergeley", "score": 87},
        {"name": "Frieda", "score": 92},
        {"name": "Fritz", "score": 40},
        {"name": "Sirius", "score": 75},
    ]
    max_score = 100
    test_name = "Python Challenge"
    context={
        "students":students,
        "test_name":test_name,
        "max_score":max_score
    }

    template = environment.get_template("result.html")
    return Response(template.render(context))
