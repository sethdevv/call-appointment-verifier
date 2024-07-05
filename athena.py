import csv
import requests

# Define your API credentials and input/output file paths
API_URL = "https://api.preview.platform.athenahealth.com/v1/XXXXX/patients"
HEADERS = {
    "Authorization": "Bearer XXXXXXXXXXXXXXX",
    "Accept": "application/json; charset=UTF-8",
}
INPUT_FILE = 'athena-input.csv'
OUTPUT_FILE = 'athena-output.csv'

# Open input and output CSV files
with open(INPUT_FILE, 'r', newline='') as csvinput, open(OUTPUT_FILE, 'w', newline='') as csvoutput:
    reader = csv.reader(csvinput)
    writer = csv.writer(csvoutput)

    # Prepare headers for output CSV
    headers = next(reader)
    headers.extend(['First Appointment', 'First Appointment Date'])
    writer.writerow(headers)

    for row in reader:
        newNumb = row[10]

        # Make API request to fetch patient data
        r = requests.get(f"{API_URL}?anyphone={newNumb}", headers=HEADERS)
        data = r.json()

        if "patients" in data:
            patients = data["patients"]

            if patients:
                patient = patients[0]
                if "firstappointment" in patient:
                    first_appointment = patient["firstappointment"]
                    row.extend(['true', first_appointment])
                else:
                    row.extend(['false', ''])
            else:
                row.extend(['false', ''])
        else:
            row.extend(['false', ''])

        # Write row to output CSV
        writer.writerow(row)
