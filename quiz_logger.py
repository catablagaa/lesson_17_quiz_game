import logging
import coloredlogs

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s | %(levelname)s | line: %(lineno)d) | %(message)s', level=logging.DEBUG)

coloredlogs.install(level='DEBUG', logger=logger)

logging.debug("Aici e un debug00")
logging.info("Aici e un info print ")
logging.warning("Aici este un warning")
logging.error("Aici e o eroare")

