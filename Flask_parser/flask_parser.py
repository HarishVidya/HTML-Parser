from Firstdraft import results
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('Index.html')

@app.route("/", methods=['POST'])
@app.route("/home", methods=['POST'])
def search():
    searchterm = request.form['searchbox']
    t = results(searchterm)    
    return render_template('Results.html', price1=t[0], price2=t[1], price3=t[2], price4=t[3], name1=t[4], name2=t[5], name3=t[6], name4=t[7], searchterm=searchterm)
    
@app.route("/about")
def about():
    return render_template('About.html')



if __name__ == '__main__':
    app.run(debug=True)