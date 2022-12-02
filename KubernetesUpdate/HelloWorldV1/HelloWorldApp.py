#!/usr/bin/env python3 

import os

# Run:
#  wget -O - -q http://localhost:8080/   to see result.  

from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def result():
  return "{\"version\": \"0.1.0\" }" # response to your request.

if __name__ == "__main__":
  os.system("ifconfig")  # Get IP address of this system 
  app.run(debug=True,host="0.0.0.0",port=8080)  # host=0.0.0.0 makes it pick all network interfaces not just loopback


