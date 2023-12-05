"""IO utils functions"""
from typing import List, Optional

def load_txt(file_path: str) -> Optional[List[str]]:
    """
    Loads txt files in a list of strings
    """
    try:
        with open(file_path, 'r') as file:
            text_lines = file.readlines()
            text_lines = [line.strip() for line in text_lines]
            return text_lines
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
