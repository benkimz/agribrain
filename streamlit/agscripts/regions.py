import os
import json

def kenyan_regions(json_file_path: str):
    
    assert os.path.exists(json_file_path), "Regions file not found"
    
    with open(json_file_path, mode="r", encoding="utf-8") as fp:
        regions = json.load(fp)
    
    assert type(regions) == list 
    
    return regions