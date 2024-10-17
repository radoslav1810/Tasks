import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    logger.info("Starting the save script...")

    # Example functionality: Saving data to a file
    try:
        with open('output.txt', 'w') as file:
            file.write('This is a test save operation.\n')
        logger.info("Data saved successfully to output.txt.")

    except Exception as e:
        logger.error("An error occurred: %s", e)


if __name__ == "__main__":
    main()
