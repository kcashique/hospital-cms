from werkzeug.wrappers import Response

from jinja2 import Environment, FileSystemLoader

from modules.db_config import db_conn
from modules.models import Doctor



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


def doctors(self, doctor_id):
    # Open a cursor to perform database operations
    if doctor_id is None:
        cur = db_conn.cursor()
        cur.execute("SELECT doctor_id, doctor_name, fee  FROM doctor_tbl;") # the excution qurry
        result = cur.fetchall() #fetch all detials and add to result
        if result is not None:
            pass
        else:
            print ("check db_connection is configured properly or db is none")
        cur.close()
        doctors_list = [{"doctor_id":row[0],  "doctor_name":row[1], "fee":row[2]} for row in result]
        print (doctor_id)
    if doctor_id is not None:
        cur = db_conn.cursor()
        cur.execute("SELECT doctor_id, doctor_name, fee  FROM doctor_tbl WHERE doctor_id=(%s);",(str(doctor_id))) # the excution qurry
        result = cur.fetchall() #fetch all detials and add to result
        if result is not None:
            pass
        else:
            print ("check db_connection is configured properly or db is none")
        cur.close()
        doctors_list = [{"doctor_id":row[0],  "doctor_name":row[1], "fee":row[2]} for row in result]
        print(doctors_list)

    test_name = "Hospitel Management System"
    context={
        "test_name":test_name,
        "doctors_list":doctors_list
    }
    template = environment.get_template("result.html")
    return Response(template.render(context), content_type='text/html')                 