from ..app import jsonify, request, app
import json
error_json = {
  400: {"status": 400, "message": "invalid parameters"},
  404: {'status': 404, "message": "not found"},
  201: {"status": 201, "message": "created"},
  409: {"status": 409, "message": "user exists"},
  200: {"status": 200, "message": "ok."}
}

class ModelEncoder(json.JSONEncoder):
  def default(self, obj):
    if hasattr(obj, "__json__"):
      return obj.__json__()
    else:
      return super().default(obj)

def model_or_404(me):
  return (jsonify(error_json[404]),404) if not me else app.response_class(
        json.dumps(me, cls=ModelEncoder),
        mimetype=app.config['JSONIFY_MIMETYPE']
    )

__api__ = {}

def api_call(mod, fn, **kwarg):
  if mod in __api__ and fn in __api__[mod]:
    return __api__[mod][fn](**kwarg)
  else:
    raise "Illegal Api Call"

def api(fn):
  fn_name = fn.__name__
  mod_name = fn.__module__.split('.')[-1]
  if mod_name not in __api__:
    __api__[mod_name] = {}
    def mod_api(name):
      def __mod_api():
        content = request.json
        param = content["param"]
        method = content["method"]
        return api_call(mod_name, method, **param)
      __mod_api.__name__ = name+"_api"
      return __mod_api
    app.route('/%s' % mod_name, methods=["POST"])(mod_api(mod_name))
  if fn_name not in __api__[mod_name]:
    __api__[mod_name][fn_name] = fn
  return fn
