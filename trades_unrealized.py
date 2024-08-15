import pandas as pd
import os
import sys
from dotenv import load_dotenv
from file_utils import FileUtils

load_dotenv()

def load_excel_dataframe(logger):
    this_method_name = sys._getframe().f_code.co_name
    file_path = "C:/Users/bhagh/Downloads/PNL_REPORT.xls"
    try:
        df = pd.read_excel(file_path, sheet_name='Sheet1', header=None)
        logger.info("Excel file loaded successfully", extra={'methodName': this_method_name})
        return df
    except Exception as exc:
        logger.error(f"Unable to read Excel file with error: {exc}", extra={'methodName': this_method_name})
        raise

def process_segment(df, segment_name, logger):
    this_method_name = sys._getframe().f_code.co_name
    try:
        segment_row = df[df.iloc[:, 0] == segment_name].index[0]
        
        header_row = segment_row + 1
        headers = df.iloc[header_row]

        # Data starts from the row after the headers
        data_start = header_row + 1
        segment_data = df.iloc[data_start:]

        # Set the correct header for the data
        segment_data.columns = headers

        # Filter out any rows where the 'Security Name' column is NaN
        segment_data = segment_data[pd.notna(segment_data['Security Name'])]
        # segment_data = segment_data[pd.notna(segment_data['Sr.'])]

        end_row = segment_data[segment_data['Sr.'].isna()].index
        if len(end_row) > 0:
            end_row = end_row[0]
            segment_data = segment_data.loc[:end_row - 1]

        # Set 'Sr.' as the index
        segment_data.set_index('Sr.', inplace=True)

        return segment_data
    except Exception as exc:
        logger.error(f"Error processing segment '{segment_name}': {exc}", extra={'methodName': this_method_name})
        return None

def main():
    this_method_name = sys._getframe().f_code.co_name

    logger = FileUtils.set_logger("PNL_REPORT")
    nas_path = os.getenv("NAS_PATH")
    output_path = f'{nas_path}/Unrealized/'
    # output_path = os.path.join(nas_path, 'Unrealized')
    FileUtils.check_and_create(output_path, logger) 

    df = load_excel_dataframe(logger)
    segments = [
        ('Equity Segment', 'Cleaned_Equity_Segment_Unrealized.csv'),
        ('Futures & Options Segment', 'Cleaned_Futures_Options_Segment_Unrealized.csv'),
        ('Commodities Segment', 'Cleaned_Commodities_Segment_Unrealized.csv')]

    # Dictionary to hold processed segment data
    processed_data = []

    for segment_name, filename in segments:
        output_file = os.path.join(output_path, filename)
        segment_data = process_segment(df, segment_name,logger)
        if segment_data is not None:
            segment_data.to_csv(output_file, index=False)
            logger.info(f"Processed and saved '{segment_name}' to '{filename}'", extra={'methodName': this_method_name})
            processed_data.append(segment_data)

    # Combine all segments into a single DataFrame
    if processed_data:
        combined_df = pd.concat(processed_data, ignore_index=True)
        combined_csv_path = os.path.join(output_path, 'Combined_Segments_Unrealized.csv')
        combined_df.to_csv(combined_csv_path, index=False)
        logger.info(f"Combined all segments into '{combined_csv_path}'", extra={'methodName': this_method_name})


if __name__ == "__main__":
    main()
