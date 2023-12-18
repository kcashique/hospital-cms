from werkzeug import Response, Request
from werkzeug.routing import Rule, Map
from werkzeug.exceptions import NotFound

from modules.routes import index, doctors, doctor_form



class HospitalSystem():
    def __init__(self):
        self.url_map=Map([
            Rule('/', endpoint='index'),
            Rule('/doctors', endpoint='doctors'),
            Rule('/doctors/<int:id>', endpoint='doctors'),
            Rule('/submit', endpoint='doctor_form')
        ])
    
    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, f'on_{endpoint}')(request, **values)   
        except NotFound:
            return Response('Not Found', status=404)
    
    def on_index(self, request):
        return index(request)
    
    def on_doctors(self, request, **values):
        doctor_id=values.get('id')
        return doctors(request, doctor_id)

    def on_doctor_form(self, request):
        return doctor_form(request)

    
def application(environ, start_response):
    request = Request(environ)
    hospital_app = HospitalSystem()
    response=hospital_app.dispatch_request(request)
    return response(environ, start_response)