from flask import  Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/email_auth')
def email_auth():
    return render_template('services/email_auth.html')

@app.route('/web_scraper')
def web_scraper():
    return render_template('services/web_scraper.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)