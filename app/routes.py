from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def view_home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def get_qr():
    if request.method == "POST":
        url = request.form.get('url')

        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, "PNG")
        buffer.seek(0)
        return send_file(buffer, mimetype="image/png", as_attachment=True, download_name="qrcode.png")
    else:
        return render_template('home.html')
