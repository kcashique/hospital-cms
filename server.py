from werkzeug import Response, Request
from werkzeug.routing import Rule, Map
from werkzeug.exceptions import NotFound

from http.cookies import SimpleCookie

from modules.routes import index, doctors, doctor_form, login

# need to impliment session

class HospitalSystem():
    def __init__(self, request):
        self.url_map=Map([
            Rule('/', endpoint=index),
            Rule('/doctors', endpoint=doctors),
            Rule('/doctors/<int:id>', endpoint=doctors),
            Rule('/create-doctor', endpoint=doctor_form),
            Rule('/login', endpoint=login)
        ])
        
        self.browser_token = self.get_token(request)

    def get_token(self, request):
        cookie = SimpleCookie(request.environ.get('HTTP_COOKIE'))
        browser_token = cookie.get('csrftoken').value 
        return browser_token
        
    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return endpoint(self, request, **values)
        except NotFound:
            return Response('Not Found', status=404)


def application(environ, start_response):
    request = Request(environ)
    hospital_app = HospitalSystem(request)
    response=hospital_app.dispatch_request(request)
    return response(environ, start_response)