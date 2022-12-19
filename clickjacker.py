#!/usr/python3 

import subprocess
import os 

if os.path.exists("curl_output"):
    os.remove("curl_output") # Checking if the file exists 


command = "read target; curl -I $target > curl_output" # Defining  the command to run


output = subprocess.check_output(command, shell=True) # Running the command and retrieving the output



print(output.decode(), "\n") # Decoding the output to a string and printing it

with open('curl_output', 'r') as file:
    # Read the contents of the file into a string
    contents = file.read()

    # Check if any of the strings are present in the contents
    if "Strict-Transport-Security" not in contents and "Content-Security-Policy" not in contents and "X-Frame-Options" not in contents and "X-Content-Type-Options" not in contents and "Referrer-Policy" not in contents and "Permissions-Policy" not in contents:
        print("\nVulnerable to Clickjacking!!!!!!")
    else:
        print("Not Vulnerable")
        
