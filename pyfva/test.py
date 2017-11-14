from pyfva.clientes.autenticador import ClienteAutenticador
import warnings

authclient = ClienteAutenticador(1,1) # negocio, entidad

if authclient.validar_servicio():
    data = authclient.solicitar_autenticacion('08-0888-0888')
else:
    warnings.warn("Autenticación BCCR No disponible", RuntimeWarning)
    data = authclient.DEFAULT_ERROR
