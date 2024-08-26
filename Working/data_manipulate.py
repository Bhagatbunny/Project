import pandas as pd
import logging
import sys
import os
from datetime import datetime
from dotenv import load_dotenv
from file_utils import FileUtils

load_dotenv()




def load_excel_dataframe(logger):
    this_method_name = sys._getframe().f_code.co_name
    file_path = "C:/Users/bhagh/Downloads/PNL_REPORT.xls"
    try:
        df = pd.read_excel(file_path)
        print("loaded excel file")
        logger.info(f"Read Excel File successfully", extra ={'methodName': this_method_name})
        return df
    except Exception as exc:
        print("error in loading excel file")
        logger.error(str(sys.exc_info()[0]) + f" Unable to Read Excel File with error: " + str(exc), extra ={'methodName': this_method_name})

def dataframe_to_csv(df, nas_path, logger):
    this_method_name = sys._getframe().f_code.co_name
    try:
        filename = f'{nas_path}/' "PNL_REPORT.csv"
        FileUtils.check_and_create(nas_path, logger)
        df.to_csv(filename, index = False)
        logger.info(f" data is written to csv", extra ={'methodName': this_method_name})
    except Exception as exc:
        logger.error(str(sys.exc_info()[0]) + f" Unable to write data to csv with error: " + str(exc), extra ={'methodName': this_method_name})

    
def main():
    nas_path = os.getenv("NAS_PATH")

    logger = FileUtils.set_logger("PNL_REPORT")
    dataframe_to_csv(load_excel_dataframe(logger), nas_path, logger)

   
if __name__ == "__main__":
    main()

