#!/usr/bin/env python3
import argparse
import csv

def most_active_cookie(filename, date):
    # Create an empty dictionary to store the count for each cookie
    cookie_count = {}
    
    # Open the CSV file and read it line by line
    try: 
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                # Get the cookie and timestamp from the row
                cookie = row[0]
                timestamp = row[1]
                
                # Check if the timestamp is from the specified date
                if timestamp.startswith(date):
                    # Get and increment the cookie count. Default value of 0 cookies
                    cookie_count[cookie] = cookie_count.get(cookie, 0) + 1

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filename}")
    except csv.Error:
        raise csv.Error(f"Error reading CSV file: {filename}")
    
    # Find the cookies with the highest count
    most_active_cookies = [cookie for cookie, count in cookie_count.items() if count == max(cookie_count.values())]
    return most_active_cookies

if __name__ == '__main__':
    # Set up the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='The name of the CSV file containing the cookie log')
    parser.add_argument('-d', '--date', required=True, help='The date to find the most active cookie for (in YYYY-MM-DD format)')
    args = parser.parse_args()
    
    # Get the most active cookie for the specified date
    most_active = most_active_cookie(args.filename, args.date)
    
    # Print the most active cookie
    for cookie in most_active:
        print(cookie)
