#from email import message
#from sre_constants import SUCCESS
#from tokenize import Name
from concurrent.futures import process
from doctest import OutputChecker
from email import message
from importlib.resources import path
from sre_constants import SUCCESS
from flask import Flask, request, render_template
import os
import numpy as np
import pandas as pd 
import subprocess
from datetime import datetime 
import os.path
from google.cloud.bigquery_storage import ReadStream
from werkzeug.wrappers import response
# initializing Flask app
app = Flask(__name__)
## @app.route('/', methods =['POST'])

#################################
###################################################################################
### Connecting to Web interface
@app.route('/')
def index():
    print("current working directory is {}".format(os.getcwd()))
    os.chdir('./dbt_pipeline_snowflake')
    print("new working directory is {}".format(os.getcwd()))
    print("list of files/dir in new working directory is {}".format(os.listdir()))
    try:
        Output=subprocess.check_output(["chmod","+x","dbt_generate_docs.sh"])
        Output=subprocess.check_output(["chmod","+x","dbt_scripts.sh"])
        Output=subprocess.check_output(["./dbt_scripts.sh"])
    except: 
        SUCCESS =35
        message = "Error in running dbt processess"
    else:
        SUCCESS =0
        message = "THe run has been successfly completed" 
    return render_template('home.html',message = message)
#######################################################################################################
### dbt docs generate will generate files such as index.html , catalog.json and manifest.json required to publish the documentation
#####################################
@app.route('/dbt_generate_docs')
def dbt_generate_docs():
    print("current working directory in dbt docs {}".format(os.getcwd()))
    try:
        Output=subprocess.check_output(["./dbt_generate_docs.sh"])
    except: 
        SUCCESS =35
        message = "Error in running dbt doc generation"
    else:
        SUCCESS =0
        if os.path.exists('./templates/index.html'):
            os.remove('./templates/index.html')
        if os.path.exists('./templates/catalogue.json'):
            os.remove('./templates/catalog.json')
        if os.path.exists('./templates/catalogue.json'):
            os.remove('./templates/manifest.json')
        try:
            Output=subprocess.check_output(["cp","./target/catalog.json","./templates"])
            Output=subprocess.check_output(["cp","./target/index.html","./templates"])
            Output=subprocess.check_output(["cp","./target/manifest.json","./templates"])
        except:
            SUCCESS =40
            message = "Error in moving index.html & supporting files to templates"
        else:
            SUCCESS =0
    if SUCCESS ==0:
        return render_template('index.html')
    else:
        return render_template('message.html',message=message)


if __name__ == "__main__":
    # serving the app directly
    app.run(debug= True)

