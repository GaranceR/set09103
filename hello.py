from flask import Flask, redirect, url_for, abort
app = Flask(__name__)

@app.route("/hello/")
def hello():
  return "Hello Sunshine! :D what is your password?"

@app.route('/static-exp/img')
def static_expl_img():
  start = '<img src="'
  url = url_for('static', filename='vmask.jpg')
  end = '">'
  return start+url+end,200

@app.route('/force404/')
def force404():
  abort(404)

@app.errorhandler(404)
def page_not_found(error):
  return "Sorry, sweetheart the page you requested couldn't be found.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

