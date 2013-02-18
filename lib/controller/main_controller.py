
class MainController:
  def __init__(self):
    pass

  def hello(self, request):
    print repr(request)
    print "HTTP Method: %s " % request.method
    return {"hello":"world", "version":"0.0.1", "attr": dir(request)}

