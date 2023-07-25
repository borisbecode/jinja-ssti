from flask import Flask, render_template_string, request, render_template
from bleach import clean
import re
app = Flask(__name__)

def clean_data(data):
    if isinstance(data, str):
        data = clean(data, tags=[], attributes={}, styles=[], strip=True)
        data = re.sub(r'[%{]', '', data)
        data = re.sub(r'[^a-zA-Z0-9]', '', data)
    return data


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = clean_data(request.form['email'])  
        try:
            
         
            return render_template('thankyou.html',email=email)
        
        except Exception as e:
            return f"Erreur : {e}"
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
    