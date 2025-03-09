import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        log_dir = os.path.join(os.getcwd(), "Logs")
        # Ensure the Logs directory exists
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)  # Create the folder if it doesn't exist

        log_file_path = os.path.join(log_dir, "automation.log")  # Log file path with name

        logger = logging.getLogger("Test")
        fileHandler = logging.FileHandler(log_file_path)  # Set log file path
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger
