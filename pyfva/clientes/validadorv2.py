'''
Alias de compatibilidad hacia atrás.

`pyfva.clientes.validador` es ahora el módulo canónico (antes "V2"); este
módulo se mantiene para que el código existente que importa `validadorv2`
siga funcionando sin cambios.
'''

from pyfva.clientes.validador import ClienteValidador  # noqa: F401
