from werkzeug.wrappers import Response

from jinja2 import Environment, FileSystemLoader

from modules.db_config import db_conn



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
    # Open a cursor to perform database operations
    cur = db_conn.cursor()
    doctors_list =[]
    result =cur.execute("SELECT doctor_name, fee FROM doctor_tbl;")
    if result is not None:
        for item in result:
            doctors_list.append(item)
    else:
        print ("check db or db_connection is not configured properly")
    cur.close()
    print (doctors_list)
    max_score = 100
    test_name = "Python Challenge"
    context={
        "students":students,
        "test_name":test_name,
        "max_score":max_score
    }
    template = environment.get_template("result.html")
    return Response(template.render(context), content_type='text/html')