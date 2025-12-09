# utils/logger.py
import logging
import pathlib

def setup_logger():
    # Carpeta donde se almacenarán los logs
    log_dir = pathlib.Path('logs')
    log_dir.mkdir(exist_ok=True)

    # Nombre del archivo de log
    log_file = log_dir / 'suite.log'

    # Configuración global del logger
    logger = logging.getLogger('TalentoLab')
    logger.setLevel(logging.INFO)

    # Evitamos duplicar handlers si se llama varias veces
    if not logger.handlers:
        # Handler para archivo
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        # Opcional: Handler para consola (para ver logs en vivo)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Instancia global para importar en los tests
logger = setup_logger()