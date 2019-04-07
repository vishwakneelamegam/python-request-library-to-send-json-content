import requests
import json
while True:
    pay = {"key":"12345"}
    r=requests.post('http://35.174.168.61:80/s',json=pay)
    c=r.content
    print (c)
    
