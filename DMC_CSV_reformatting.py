import csv

def convert_csv(input_file, output_file):
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        rows = list(csv_reader)

    with open(output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerows(rows)

    print(f"Conversion complete. Converted file saved as {output_file}")

# Example usage
input_file = ""  # Replace with your input file path
output_file = "" # Replace with your desired output file path
convert_csv(input_file, output_file)
