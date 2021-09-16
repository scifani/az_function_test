import json

data = {
  "firstname":"simone",
  "lastname": "cifani",
  "age": 38
}

return json.dumps(data, indent=2)
