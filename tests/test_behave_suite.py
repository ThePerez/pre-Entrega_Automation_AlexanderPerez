# tests/test_behave_suite.py

import subprocess
import os
import logging

logger = logging.getLogger('pytest')

"""

    reports_path = os.path.join(os.getcwd(), 'reports')
    os.makedirs(reports_path, exist_ok=True)
    
    # Comando como cadena simple para evitar problemas de lista/subprocess
    command_string = 'behave -t @smoke,@regression -f json -o reports/behave.json -q'
    
    logger.info(f"Ejecutando Behave con comando: {command_string}")

    # Ejecutar el comando con shell=True para robustez en Windows
    result = subprocess.run(command_string, shell=True) 

    # Validar: Si Behave tiene fallos, Pytest debe fallar.
    assert result.returncode == 0, f"La suite BDD de Behave falló. Código de salida: {result.returncode}"
    
    logger.info("La suite BDD ejecutada por Behave terminó exitosamente.")  

"""
