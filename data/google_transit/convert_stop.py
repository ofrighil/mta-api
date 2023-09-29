import csv

output_file = ['stop_id_to_name = {']

with open('stops.txt', 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        output_file.append(
            f'    \'{row["stop_id"]}\': \"{row["stop_name"]}\",'
        )
    output_file.append('}')

with open('stops.py', 'w') as f:
    f.write('\n'.join(output_file))
