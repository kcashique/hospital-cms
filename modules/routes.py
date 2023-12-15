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


def doctors(self):
    # Open a cursor to perform database operations
    cur = db_conn.cursor()
    result_list =[]
    cur.execute("SELECT * FROM doctor_tbl;") # the excution qurry
    result = cur.fetchall() #fetch all detials and add to result
    if result is not None:
        for item in result:
            result_list.append(item)
    else:
        print ("check db_connection is configured properly")
    cur.close()
    # doctors_list = [{"doctor_name":name, "fee":value} for name, value in result_list]
    doctors_list = [
        Doctor(doctor_id=row[0], doctor_name=row[1], speciality=row[2], fee=row[3], scheduled_time=row[4], entry_date=row[5])
        for row in result
    ]
    print (doctors_list)
    # showing attribute error
    response_data = "\n".join([f"{doctor.doctor_name}: {doctor.fee}" for doctor in doctors_list])
    print (response_data)

    test_name = "Hospitel Management System"
    context={
        "test_name":test_name,
        "doctors_list":doctors_list
    }
    template = environment.get_template("result.html")
    return Response(template.render(context), content_type='text/html')