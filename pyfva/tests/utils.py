from http.client import HTTPSConnection, HTTPConnection
import json
import ssl
import os
import base64
import time
from pathlib import Path

def read_files(_format,  post_read_fn=lambda x: base64.b64encode(x).decode(), name='test.'):
    defaultpath = Path('testdata/')
    f = None
    fpath = None
    if _format == 'xml_cofirma':
        fpath = defaultpath / "test.xml"
    elif _format == 'xml_contrafirma':
        fpath = defaultpath / "ctest.xml"
    elif 'odf' == _format:
        fpath = defaultpath  / "test.odt"
    elif 'msoffice' == _format:
        fpath = defaultpath / "test.docx"
    elif 'pdf' == _format:
        fpath = defaultpath / "test.pdf"
    else:
        fpath = defaultpath / (name+_format)
    with open(fpath, 'rb') as arch:
        f = arch.read()
    return post_read_fn(f)

def http_testing_get(request_url):
    host = 'localhost'
    connection = HTTPConnection(host, port=8000)
    connection.request(method="GET", url=request_url)
    # Print the HTTP response from the IOT service endpoint
    response = connection.getresponse()

    data = json.loads(response.read())
    connection.close()
    return data

def https_get(request_url):

    certificate_file = os.getenv('REQUESTS_CERT_PATH', '')
    certificate_secret = os.getenv('REQUESTS_KEY_PATH', '')

    host = 'localhost'
    request_headers = {'Content-Type': 'application/json'}

    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.load_cert_chain(certfile=certificate_file, keyfile=certificate_secret)

    # Create a connection to submit HTTP requests
    connection = HTTPSConnection(host, port=8443, context=context)

    # Use connection to submit a HTTP GET request
    connection.request(method="GET", url=request_url, headers=request_headers)

    # Print the HTTP response from the IOT service endpoint
    response = connection.getresponse()
    data = json.loads(response.read())
    connection.close()
    return data


def http_get(request_url):
    debug_server = os.getenv('DEBUG_HTTP_SERVER', None)
    if debug_server is not None:
        debug_server = int(debug_server)
        if debug_server:
            return http_testing_get(request_url)
    return https_get(request_url)

class CheckReception:
    def check_reception(self, idtransaction):
        request_url = '/check_transaction/' + str(idtransaction)
        counter = 0
        ok = False
        response = {'codigo_error': 1}
        while not ok and counter < 10:
            try:
                response = http_get(request_url)
                if response['ok']:
                    ok = True
                else:
                    counter += 1
            except Exception as e:
                print(e)
                counter += 1
                time.sleep(2)
        return response
