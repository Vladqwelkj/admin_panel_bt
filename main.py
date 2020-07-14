from flask import Flask, render_template
import requests

app = Flask(__name__)



WEB_ADDRESSES_TO_CHECK = ['http://92.38.160.45:8080/log', 0]

def get_page_html_body(self, address):
    html = requests.get(address).text
    html_body = html.split('<body>')[1].split('</body>')[0]
    return html_body


@app.route('/')
def main_page():
    global WEB_ADDRESSES_TO_CHECK
    addresses_and_html_body = []
    for address in WEB_ADDRESSES_TO_CHECK:
        try:
            html_body = get_page_html_body(address)
            addresses_and_html_body.append((address, html_body))
        except:
            pass
    return render_template('index.html',
        addresses_and_html_body=addresses_and_html_body)


if __name__=='__main__':
    app.run('0.0.0.0', '5050')