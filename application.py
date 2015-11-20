
import os
import sys
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
  bk = os.environ['BEACON_KEY']
  return render_template('index.html', beacon_key=bk)

if __name__ == '__main__':
  app.run()
