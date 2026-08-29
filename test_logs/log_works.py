import logging
from logging import basicConfig

basicConfig(
    level=logging.DEBUG,
    filename="logs.log",
    filemode="a",
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)

logger.debug("Debug")
logger.info("Info")
logger.warning("Warning")
logger.error("Error")
logger.critical("Critical")


