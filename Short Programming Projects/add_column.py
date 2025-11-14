import csv

def read_ids(filename):
    id_name_dict = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row: 
                id_key = row[0]
                name_value = row[1]
                id_name_dict[id_key] = name_value
    return id_name_dict

def add_name_column(txt_filename, id_names_dict):
    output_filename = "output_" + txt_filename
    
    try:
        with open(txt_filename, 'r') as infile, \
             open(output_filename, 'w') as outfile:
            
            for line in infile:
                parts = line.strip().split('\t')
                
                if len(parts) == 2:
                    id_val = parts[0]
                    city_val = parts[1]
                    
                    name_val = id_names_dict.get(id_val, "NAME_NOT_FOUND")
                    
                    outfile.write(f"{id_val},{name_val},{city_val}\n")
                    
    except:
        print('ERROR')