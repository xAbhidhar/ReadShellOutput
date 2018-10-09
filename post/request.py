import requests

requests.post("http://127.0.0.1:8080/commands", params={'filename':'commands.txt'})