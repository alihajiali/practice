import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM4ODEzMzA2LCJpYXQiOjE2Mzg4MTMwMDYsImp0aSI6IjYzODVjYTdhNzQ1NjRlY2ZiMzBhYjIxNmNjYWQ3MTU1IiwidXNlcl9pZCI6MX0.Tz_1EBZ9wakJ2Ty6aQD_Z31JYYsnuRUluMckfMLMkI0'

r = requests.get('http://127.0.0.1:8082/api/post/', headers=headers)

print(r.text)