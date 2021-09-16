import json

async def main(req: func.HttpRequest) -> func.HttpResponse:
  """
  The main entry point to the function.
  """
    
  data = {
    "firstname":"simone",
    "lastname": "cifani",
    "age": 38
  }

  return func.HttpResponse(data, mimetype="application/json")
