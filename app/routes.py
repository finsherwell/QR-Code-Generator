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
        # Retrieve settings from form
        url = request.form.get('url')
        filetype = request.form.get('filetype', 'PNG')
        download_name = request.form.get('download_name', 'qrcode')
        fill_color = request.form.get('fill_color', 'black')
        back_color = request.form.get('back_color', 'white')

        # Generate the QR code with specified settings
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        # Prepare the image buffer
        buffer = BytesIO()
        img.save(buffer, format=filetype)
        buffer.seek(0)

        # Set the file extension based on file type
        extension = filetype.lower()
        download_filename = f"{download_name}.{extension}"

        return send_file(buffer, mimetype=f"image/{extension}", as_attachment=True, download_name=download_filename)
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
