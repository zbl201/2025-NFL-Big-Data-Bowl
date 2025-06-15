
from pathlib import Path
import os

## Printing To text for debugging
def print_to_text(filename: str, to_text: str):    
    path = f"debug/{filename}.txt"
    file_path = Path(path)
    if file_path.exists():
        with open(path, 'a') as file:
            file.write(to_text)
            file.write('\n')
            file.write('\n')
    else:
        with open(path, 'w') as file:
            file.write(to_text)
            file.write('\n')
            file.write('\n')
    

    
    
    
