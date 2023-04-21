import shutil
import os
import logging
import time
import sys

# Please make sure the directories are in this format c:/User/test

main_folder = sys.argv[1]
copy_folder = sys.argv[2]
log_file = sys.argv[3]
interval = int(sys.argv[4])

logging.basicConfig(filename=log_file,
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

while True:
    temp_files = []
    for main_dirs, sub_dirs, files in os.walk(main_folder):
        if len(files) == 0:

            # print("the file you tried to copy was empty")
            for check, copy_dirs, check_files in os.walk(copy_folder):
                for check_file in check_files:
                    os.remove(os.path.join(check, check_file))
                    logger.info(check_file + " was deleted")
                    print(check_file + " was deleted")

        for file in files:
            filename = os.path.join(main_folder, main_dirs, file)
            temp_files.append(filename)

            shutil.copy(filename, copy_folder)
            logger.info(file + " was successfully copied to " + copy_folder)
            print(file + " was successfully copied to " + copy_folder)

            for check, copy_dirs, check_files in os.walk(copy_folder):
                for check_file in check_files:
                    if not os.path.exists(os.path.join(main_folder, check_file)):
                        os.remove(os.path.join(check, check_file))
                        logger.info(check_file + " was deleted")
                        print(check_file + " was deleted")
                    continue

    time.sleep(interval)
    i = 0
    empty = False
    for main_dirs, sub_dirs, files in os.walk(main_folder):
        for file in files or i < len(temp_files):
            filename = os.path.join(main_folder, main_dirs, file)
            if len(temp_files) == 0:
                print(filename + " was created")
                logger.info(filename + " was created")
                empty = True

            if not empty:
                if not temp_files[i] == filename:
                    print(file + " was created")
                    logger.info(file + " was created")
                    continue
            i += 1
