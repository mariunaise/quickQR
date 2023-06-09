from flask import Flask, send_file, request, render_template
import qrcode 
import io
import base64

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    data = request.form['text']
    img = qrcode.make(data)
    buf = io.BytesIO()
    img.save(buf, "PNG")
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode('ascii')
    return render_template('image.html', img_data=img_str)
    

if __name__ == "__main__":
    app.run()