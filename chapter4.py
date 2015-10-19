from flask import Flask, request, url_for
app = Flask(__name__)

@app.route("/")
def root():
  return "Hello Napier"

@app.route("/display/")
def display():
  start = '<img src="'
  url = url_for('static',filename='new_image.png')
  end = '">'
  return start + url + end, 200
  
@app.route("/account/", methods=['GET','POST'])
def account():
  if request.method == 'POST':
    f = request.files['datafile']
    f.save('static/new_image.png')
    return "File uploaded!"
  else:
    page ='''
    <html><body>
      <form action="" method="post" name="form" enctype="multipart/form-data">
        <input type="file" name ="datafile" />
        <input type="submit" name="submit" id="submit"/>
      </form>
    </body></html>'''

    return page, 200

@app.route("/hello/")
def hello():
  name = request.args.get('name','')
  if name == '':
    return "You didn't enter your name"
  else:
    return "Hello %s" % name

@app.route("/add/<int:first>/<int:second>")
def add(first,second):
  return str(first+second)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
