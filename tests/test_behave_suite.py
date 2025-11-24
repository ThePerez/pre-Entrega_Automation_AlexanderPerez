import subprocess
import os
import logging

logger = logging.getLogger('pytest')

def test_behave_suite():  
    # 1. Asegura que el directorio reports exista
    reports_path = os.path.join(os.getcwd(), 'reports')
    os.makedirs(reports_path, exist_ok=True)
    
    # 2. Define el comando de ejecución (behave -t @smoke,@regression -f json -o reports/behave.json)
    command = [
        'behave', 
        '-t', '@smoke,@regression', 
        '-f', 'json', 
        '-o', 'reports/behave.json',
        '-q' # Modo silencioso
    ]
    
    logger.info(f"Ejecutando Behave con comando: {' '.join(command)}")

    # 3. Ejecutar el comando Behave
    result = subprocess.run(command)

    # 4. Validar: Si Behave tiene fallos, Pytest debe fallar (código de retorno 0 = éxito)
    assert result.returncode == 0, f"La suite BDD de Behave falló. Código de salida: {result.returncode}"
    
    logger.info("La suite BDD ejecutada por Behave terminó exitosamente.")