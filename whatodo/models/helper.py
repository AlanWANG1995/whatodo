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

