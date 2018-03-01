#!/bin/bash
OLDPWD=`pwd`
cd ../
python -c "import pyfva; print(pyfva.constants.show_constants())" > docs/source/formatos_en_fva.rst
cd $OLDPWD
make html

