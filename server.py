from werkzeug import Response, Request
from werkzeug.routing import Rule, Map
from werkzeug.exceptions import NotFound

from modules.routes import index, doctors



class HospitalSystem():
    def __init__(self):
        self.url_map=Map([
            Rule('/', endpoint='index'),
            Rule('/doctors', endpoint='doctors')
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
    
    def on_doctors(self, request):
        return doctors(request)

    
def application(environ, start_response):
    request = Request(environ)
    hospital_app = HospitalSystem()
    response=hospital_app.dispatch_request(request)
    return response(environ, start_response)