#!/usr/bin/env python3
import json
import re
import itertools
from adwaita_colors import get_adwaita_colors
from adwaita_ui_colors import get_adwaita_ui_colors


def load_jsonc(path):
    '''Read JSON with comments.'''
    original = open(path).read()
    stripped = re.sub(r'[^:]//.+$', '', original, flags=re.MULTILINE)
    return json.loads(stripped)


def get_default_syntax_colors():
    return load_jsonc(f'default_themes/dark.jsonc')['tokenColors']


extra_syntax_colors = [
    {
        'scope': ['markup.italic.markdown'],
        'settings': {
            'fontStyle': 'italic'
        }
    },
    {
        'scope': ['markup.strikethrough.markdown'],
        'settings': {
            'fontStyle': 'strikethrough'
        }
    }
]

package_json_entry = {
    'contributes': {
        'themes': []
    }
}

name = 'fekoneko-theme'
ui_colors = get_adwaita_ui_colors()
syntax_colors = get_default_syntax_colors()

theme = {
    '$schema': 'vscode://schemas/color-theme',
    'name': name,
    'type': 'light',
    'colors': ui_colors,
    'tokenColors': syntax_colors
}

file_name = f'{name.lower().replace(" ", "-").replace("-&-", "-")}.json'
json.dump(theme, open(f'../themes/{file_name}', 'w'), indent=2)

package_json_entry['contributes']['themes'].append({
    'label': name,
    'uiTheme': 'vs-dark',
    'path': f'./themes/{file_name}'
})
