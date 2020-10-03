import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)  # filehandler object

    logger.setLevel(logging.CRITICAL)
    logger.debug("A debug statement is executed")
    logger.info("Information! statement")
    logger.warning("Warning! - Something went wrong")
    logger.error("Major error! Assertions failed")
    logger.critical("Critical Error")
