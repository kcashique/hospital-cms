from werkzeug.wrappers import Response

def index(self):
    data = 'hello World!'
    return Response(data)