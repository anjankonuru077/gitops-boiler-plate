import csv

csv_file = r'C:\Users\anjan\Downloads\Terraform_Projects\projects-1\variables.csv'
tfvars_file = r'C:\Users\anjan\Downloads\Terraform_Projects\projects-1\variables.tfvars'

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    variables = next(reader)

with open(tfvars_file, 'w') as file:
    for key, value in variables.items():
        file.write(f'{key} = "{value}"\n')