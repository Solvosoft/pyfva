#/bin/sh

DIRDIA=diagramas
mkdir -p $DIRDIA
pyreverse -f ALL -a 1 pyfva.clientes
mv packages.dot $DIRDIA/clientes_packages.dot
mv classes.dot $DIRDIA/clientes_classes.dot

pyreverse -f ALL -a 1  pyfva.receptor
mv packages.dot $DIRDIA/receptor_packages.dot
mv classes.dot $DIRDIA/receptor_classes.dot

pyreverse -f ALL -a 1  pyfva.soap
mv packages.dot $DIRDIA/soap_packages.dot
mv classes.dot $DIRDIA/soap_classes.dot
