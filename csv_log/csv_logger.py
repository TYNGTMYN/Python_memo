import csv
import os

def open_csv(filename):
    """
    Opens a csv file and returns a object of csv writer
    """
    if os.path.exists(filename):
        csv_file = open(filename, 'a')
    else:
        csv_file = open(filename, 'w')
    return csv_file

def write_csv(csv_file, data):
    """
    Writes data to csv file
    """
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(data)

def close_csv(csv_file):
    """
    Closes csv file
    """
    csv_file.close()

def conv_list_to_str(data):
    """
    Converts list to string
    """
    return ','.join(data)

def write_log_to_csv(filename, data):
    """
    Writes data to csv file
    """
    csv_writer = open_csv(filename)
    write_csv(csv_writer, data)
    close_csv(csv_writer)

def write_log_main(data):
    """
    Main function of this Logger
    """
    filename = "log.csv"
    write_log_to_csv(filename, data)
