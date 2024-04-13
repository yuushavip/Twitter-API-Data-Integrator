import csv
import os

def get_data_path(file_name):
    data_path = f"data/{file_name}"
    
    return data_path

def write_to_csv(data_items, file_name, mode, keys=None):
    file_path = get_data_path(file_name)
    
    if not data_items:
        return
    
    if not keys:
        keys = data_items[0].keys()
    
    with open(file_path, mode, newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        
        if os.path.getsize(file_path) == 0:
            writer.writeheader()
        
        writer.writerows(data_items)