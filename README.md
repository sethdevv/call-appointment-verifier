# Call / Appointment Verifier

1. **Imports**: The script imports necessary modules: `csv`, `requests`, and `json`.

2. **API Endpoint and Headers**: 
   - Defines `API_ENDPOINT` as the URL for the Athenahealth API endpoint to fetch patient data.
   - Sets `HEADERS` with authorization details and specifies the expected response format.

3. **Function Definition (`get_first_appointment`)**:
   - Takes a `phone_number` parameter.
   - Constructs a request to the Athenahealth API to retrieve patient data based on the provided phone number.
   - Extracts the first appointment date of the patient if available and returns it.

4. **File Paths**:
   - Defines `input_file` and `output_file` for reading input data (CSV) and writing output data (CSV), respectively.

5. **Main Processing**:
   - Opens the input CSV file for reading and the output CSV file for writing.
   - Initializes `reader` for reading from the input CSV and `writer` for writing to the output CSV.

6. **Processing Each Row**:
   - Reads and processes each row from the input CSV file.
   - Extracts the phone number from the appropriate column (`row[10]`).
   - Calls `get_first_appointment` function to fetch the first appointment date for the patient associated with the phone number.
   - Appends information (whether a first appointment exists and its date) to each row.
   - Collects all rows (including the header with additional columns) into `all_rows` list.

7. **Writing to Output**:
   - Writes all collected rows (`all_rows`) to the output CSV file using the `writer` object.

8. **Completion**:
   - Closes both input and output files once all processing is complete.

This script essentially reads patient phone numbers from an input CSV file, queries Athenahealth's API to retrieve information about the patients (specifically their first appointment dates), and then writes this information (along with additional flags) back into an output CSV file. It's useful for batch processing and updating records with additional patient information fetched from an external API.
