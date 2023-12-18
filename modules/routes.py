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
    doctor_list=[]
    try:
        if doctor_id is None:
            cur = db_conn.cursor()
            cur.execute("SELECT doctor_id, doctor_name, fee  FROM doctor_tbl;") # the excution qurry
            result = cur.fetchall() #fetch all detials and add to result
            if result is not None:
                pass
            else:
                print ("check db_connection is configured properly or db is none")
            cur.close()
            if len(result)==0:
                print("No Data present in the given id")
                raise ValueError(f'result_list={result}', "No Data present in database")

            else:
                    doctors_list = [{"doctor_id":row[0],  "doctor_name":row[1], "fee":row[2]} for row in result]
        if doctor_id is not None:
            cur = db_conn.cursor()
            cur.execute("SELECT doctor_id, doctor_name, fee  FROM doctor_tbl WHERE doctor_id=(%s);",(str(doctor_id))) # the excution qurry
            result = cur.fetchall() #fetch all detials and add to result
            if result is not None:
                pass
            else:
                print ("check db_connection is configured properly or db is none")
            cur.close()
            if len(result)==0:
                print("No Data present in the given id")
                raise ValueError(f'result_list={result}', "No Data present in the given id")
            else:
                doctors_list = [{"doctor_id":row[0],  "doctor_name":row[1], "fee":row[2]} for row in result]
        test_name = "Hospitel Management System"
        context={
            "test_name":test_name,
            "doctors_list":doctors_list
        }
        template = environment.get_template("result.html")
        return Response(template.render(context), content_type='text/html')
    except ValueError as err:
        print (f"Data_Error :{err}")
        resp= f"Data_Error :{err}"
        return Response(resp, content_type='text/html', status=404)


def doctor_form(request):
    if request.method == 'POST':
        doctor_name= request.form.get('doctor_name')
        speciality = request.form.get('speciality')
        fee = request.form.get('fee')
        scheduled_time =request.form.get('scheduled_time')

        print(f'{doctor_name}, {speciality}, {fee}, {scheduled_time}')
        resp="Form sumbited succes"
        context={
            "resp":resp,
        }
        template = environment.get_template("doctors_form.html")
        return Response(template.render(context), content_type='text/html')
    else:
        template = environment.get_template("doctors_form.html")
        return Response(template.render(), content_type='text/html')