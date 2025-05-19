import time
import logging
from src.library.dependency.core.container import Container
from src.library.dependency.core.loader import resolve_dependency
from src.library.utils import load_env
from src.app.module import MainModule

logger = logging.getLogger("MainApplication")

class MainApplication():
    init_time = time.time()
    load_env(".env.yaml")
    
    def __init__(self) -> None:
        super().__init__()

        container = Container.empty()
        resolve_dependency(container, appmodule=MainModule)
        logger.info(f"Application started in {time.time() - self.init_time} seconds")

    def loop(self) -> None:
        logger.info("Starting loop for Main Application")
        while True:
            time.sleep(1)