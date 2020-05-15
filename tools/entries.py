#!/usr/bin/env python3
"""
Displays entry count for status codes
"""

import sys
import os
import json
from typing import Optional, Dict, Any, List

from rich.console import Console
from rich.table import Table
from rich.rule import Rule
from rich.text import Text

CONSOLE = Console()


def _get_code_map() -> Dict[str, List[Dict[str, Any]]]:
    """Fills up a full map from the JSON files"""
    code_map = {'official': [], 'unofficial': []}
    for root, _, files in os.walk('codes'):
        for json_file in [file for file in files if '.json' in file]:
            with open(os.path.join(root, json_file), 'r') as jf:
                code_data = json.load(jf)
            if '/official' in root:
                code_map['official'].append(code_data)
            else:
                code_map['unofficial'].append(code_data)
    return code_map


def _print_table(label: str, color: str, data: List[Dict[str, Any]]) -> None:
    empty_codes = []
    table = Table(title=label, title_style=f'bold {color}', header_style=f'bold {color}')
    table.add_column('Code')
    table.add_column('Description')
    table.add_column('Haikus')
    for item in data:
        if item['messages']:
            table.add_row(str(item['code']), item['name'], str(len(item['messages'])))
        else:
            empty_codes.append(item['code'])
    if table.row_count:
        CONSOLE.print(table)
    else:
        CONSOLE.print(label, style=f'bold {color}')
    CONSOLE.print("Empty Codes:", style=f'bold {color}')
    empty = Text(", ".join([str(x) for x in empty_codes]))
    CONSOLE.print(empty)


def get_all_codes() -> None:
    """Returns all Codes and their counts -- groups Codes with 0"""
    code_map = _get_code_map()
    _print_table('Official Codes', 'green', code_map['official'])
    CONSOLE.print(Rule(style='bold white'))
    _print_table('Unofficial Codes', 'yellow', code_map['unofficial'])


def get_empty_codes() -> None:
    """Returns all Codes that have no haikus"""
    code_map = _get_code_map()
    official = [
        f"{code['code']} {code['name']}"
        for code in code_map['official']
        if not code['messages']
    ]
    unofficial = [
        f"{code['code']} {code['name']}"
        for code in code_map['unofficial']
        if not code['messages']
    ]
    table = Table(title='CODES WITHOUT HAIKUS', title_style='bold white')
    table.add_column('Official', header_style='bold green', style='green')
    table.add_column('Unofficial', header_style='bold yellow', style='yellow')
    for pair in zip(official, unofficial):
        table.add_row(pair[0], pair[1])
    CONSOLE.print(table)


def main(command: Optional[str] = None) -> None:
    """Processes command to decide what to return"""
    if 'tools' in os.getcwd():
        os.chdir('..')
    if command and command == 'empty':
        get_empty_codes()
    else:
        get_all_codes()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('Usage:  "entries.py" or "entries.py empty"')
        sys.exit(1)
