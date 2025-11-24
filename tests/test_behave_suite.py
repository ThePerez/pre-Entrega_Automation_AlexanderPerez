import subprocess
import os
import logging

logger = logging.getLogger('pytest')

def test_behave_suite():  
    reports_path = os.path.join(os.getcwd(), 'reports')
    os.makedirs(reports_path, exist_ok=True)
    
    # 2. Define el comando como UNA SOLA CADENA.
    command_string = 'behave -t @smoke,@regression -f json -o reports/behave.json -q'
    
    logger.info(f"Ejecutando Behave con comando: {command_string}")

    # 3. Ejecutar el comando con shell=True
    result = subprocess.run(command_string, shell=True) # <-- CAMBIO CRUCIAL

    # 4. Validar: Si Behave tiene fallos, Pytest debe fallar.
    assert result.returncode == 0, f"La suite BDD de Behave falló. Código de salida: {result.returncode}"
    
    logger.info("La suite BDD ejecutada por Behave terminó exitosamente.")