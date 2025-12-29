from datetime import datetime

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route("/privacy")
def privacy():
    context = {
        'site_name': 'Dan\'s App',
        'company_name': 'Dan one person limited company',
        'contact_email': 'privacy@yourapp.com',
        'company_address': '123 Tech Street, San Francisco, CA 94107',
        'last_updated': datetime.now().strftime('%Y-%m-%d'),
        'current_year': datetime.now().year,
    }
    return render_template('privacy.html', **context)


@app.route('/terms')
def terms():
    context = {
        'site_name': 'Dan\'s App',
        'company_name': 'Dan one person limited company',
        'contact_email': 'privacy@yourapp.com',
        'company_address': '123 Tech Street, San Francisco, CA 94107',
        'last_updated': datetime.now().strftime('%Y-%m-%d'),
        'current_year': datetime.now().year,
    }
    return render_template('terms.html', **context)


if __name__ == "__main__":
    app.run(debug=False)
