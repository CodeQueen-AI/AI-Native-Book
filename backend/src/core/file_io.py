"""
Utility functions for file operations within the backend.
"""

import os
from typing import List

def read_file_content(file_path: str) -> str:
    """Reads the content of a file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def list_markdown_files(directory: str) -> List[str]:
    """Lists all markdown files in a given directory and its subdirectories."""
    markdown_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
    return markdown_files
