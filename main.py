# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:12:28 2020

@author: rajakishorekavi
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    #msg.append("Hi, I'm chatbot. Ask me anything.")
    return "Successfully installed all the Libraries and is running. Upload the files now"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)
