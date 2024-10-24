import logging
import argparse
import os
import shutil
from pyats.easypy.plugins.bases import BasePlugin

logger = logging.getLogger(__name__)
logger.info("Starting CopyReportPlugin loading...")

class CopyReportPlugin(BasePlugin):
    name = 'CopyReport'
    parser = argparse.ArgumentParser(add_help=False)

    def __init__(self, *args, **kwargs):
        self.directory = kwargs.pop('directory', './default_directory')
        super().__init__(*args, **kwargs)

    def post_job(self, job):
        if not job.runtime.testbed:
            logger.error("No testbed provided in the job.")
            return

        testbed = job.runtime.testbed
        source_directory = testbed.custom.get('directory', './default_directory')
        destination_directory = self.directory
        report_file = os.path.join(source_directory, 'test_file.txt')
        destination = os.path.join(destination_directory, 'test_file.txt')

        if os.path.exists(report_file):
            shutil.copy(report_file, destination)
            logger.info(f"Report copied to {destination}")
        else:
            logger.error(f"Report file {report_file} not found!")