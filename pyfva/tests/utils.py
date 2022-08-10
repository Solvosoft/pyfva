from http.client import HTTPSConnection, HTTPConnection
import json
import ssl
import os
import base64
import time
from pathlib import Path
import hashlib

def get_digest(digest_name):
    if 'sha256' == digest_name:
        return hashlib.sha256()
    elif 'sha384' == digest_name:
        return hashlib.sha384()
    elif 'sha512' == digest_name:
        return hashlib.sha512()

def get_hash_sum(data, algorithm, b64=False):
    if type(data) == str:
        data = data.encode()
    digest = get_digest(algorithm)
    digest.update(data)
    if b64:
        return base64.b64encode(digest.digest()).decode()
    hashsum = digest.hexdigest()
    return hashsum

def read_files(_format,  post_read_fn=lambda x: base64.b64encode(x).decode(),
               name='test.', b64=True):
    defaultpath = Path('testdata/')
    f = None
    fpath = None
    if _format == 'xml_cofirma':
        fpath = defaultpath / "test.xml"
    elif _format == 'bom':
        fpath = defaultpath / "bom.xml"
    elif _format == 'xml_contrafirma':
        fpath = defaultpath / "contrafirmado.xml"
    elif _format == 'nocontrafirma':
        fpath = defaultpath / "no_contrafirmado.xml"
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
        HASH = get_hash_sum(f, 'sha512', b64=b64)
    return post_read_fn(f), HASH


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
                    time.sleep(1)
            except Exception as e:
                print(e)
                counter += 1
                time.sleep(2)
        return response
