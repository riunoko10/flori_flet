import logging

def configure_logger():
    # Configurar el logger
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("floristeria.log"),
            logging.StreamHandler()
        ]
    )

def get_logger(name):
    configure_logger()
    return logging.getLogger(name)