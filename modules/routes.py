from werkzeug.wrappers import Response

def index(self):
    data = 'hello World!'
    return Response(data)

def doctors(self):
    data = str(["ashique", "mubeen", "shanib","shabeeb"])
    return Response(data)