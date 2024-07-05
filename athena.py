import csv
import requests
import json

# Define API endpoint and headers
API_ENDPOINT = "https://api.preview.platform.athenahealth.com/v1/18802/patients"
HEADERS = {
    "Authorization": "Bearer XXXXXXXXXXXXXXX",
    "Accept": "application/json; charset=UTF-8",
}

def get_first_appointment(phone_number):
    params = {
        "anyphone": phone_number
    }
    response = requests.get(API_ENDPOINT, headers=HEADERS, params=params)
    data = response.json()
    
    if "patients" in data and len(data["patients"]) > 0:
        patient = data["patients"][0]
        if "firstappointment" in patient:
            return patient["firstappointment"]
        elif len(data["patients"]) > 1 and "firstappointment" in data["patients"][1]:
            return data["patients"][1]["firstappointment"]
    
    return None

# Input and Output file paths
input_file = 'athena-input.csv'
output_file = 'athena-output.csv'

# Open input and output files
with open(input_file, 'r') as csvinput, open(output_file, 'w', newline='') as csvoutput:
    reader = csv.reader(csvinput)
    writer = csv.writer(csvoutput)
    
    # Initialize output data structure
    all_rows = []
    
    # Process header row
    header = next(reader)
    header.extend(['First Appointment', 'First Appointment Date'])
    all_rows.append(header)
    
    # Process each row in the input CSV
    for row in reader:
        phone_number = row[10]
        first_appt = get_first_appointment(phone_number)
        
        if first_appt:
            row.append('true')
            row.append(first_appt)
        else:
            row.append('false')
            row.append('')
        
        all_rows.append(row)
    
    # Write all rows to output CSV
    writer.writerows(all_rows)
