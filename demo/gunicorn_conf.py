import os
import pathlib

current_dir = pathlib.Path(__file__).resolve().parent
# Configuraciones
bind = '0.0.0.0:8443'
workers = os.getenv('NUM_WORKERS', 2)  # Cambia el valor por defecto según sea necesario
timeout = 180
name = os.getenv('NAME', 'pyfva')  # Cambia el valor por defecto según sea necesario
loglevel = 'debug'
cert_dirs = str(os.getenv('CERTSDIR', current_dir / "../certs").absolute().resolve())

accesslog = os.path.join(os.getenv('LOGDIR', '/var/log/pyfva'), 'access_gunicorn.log')
errorlog = os.path.join(os.getenv('LOGDIR', '/var/log/pyfva'), 'gunicorn.log')
keyfile = os.getenv('REQUESTS_KEY_PATH', cert_dirs + '/bccr_agent_key.pem')  # Cambia según corresponda
certfile = os.getenv('REQUESTS_CERT_PATH', cert_dirs +'/bccr_agent.pem')  # Cambia según corresponda
ca_certs = os.getenv('REQUESTS_CA_PATH', cert_dirs +'/ca_nacional_de_CR.pem')  # Cambia según corresponda

def ssl_context(conf, default_ssl_context_factory):
    import ssl
    context = default_ssl_context_factory()
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    return context


# Opciones SSL
do_handshake_on_connect = True
#ssl_version = 'TLSv1_2'  # Forzar TLS 1.2
ciphers = 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-GCM-SHA384:AES256-SHA256:AES128-SHA256'
