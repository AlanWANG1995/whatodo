import requests
def json(path:str, method:str, param:dict):
  r = requests.post("http://127.0.0.1:5000/%s" % path, json={
    "method": method,
    "param": param
  })
  if r.status_code == 200:
    return r.json()

json('user', 'create', {'email': 'alanwang.lan@gmail.com'})
r = json('user', 'show', {'email': 'alanwang.lan@gmail.com'})
uuid = r['uuid']