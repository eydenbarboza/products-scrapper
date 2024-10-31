import unicodedata
import re

def remove_accents(value: str) -> str:
    value = unicodedata.normalize('NFD', value)
    value = ''.join(c for c in value if unicodedata.category(c) != 'Mn')
    return value

def convert_to_lowercase(value: str) -> str:
    value = value.lower()
    return value


def remove_special_chars(value: str) -> str:
    value = re.sub(r'[^a-z0-9\s]', '', value)
    return value

def remove_extra_spaces(value: str) -> str:
    value = ' '.join(value.split())
    return value

def clean_text(value: str) -> str:

    if value is None:
        return None
    
    value = remove_accents(value)
    value = convert_to_lowercase(value)
    value = remove_special_chars(value)
    value = remove_extra_spaces(value)
    return value

def clean_options(options: list, exclude_options: list = None):
    """
    Cleans a list of options by removing whitespace and irrelevant options.

    :param options: Lista de opciones a limpiar.
    :param exclude_options: Lista de opciones irrelevantes a excluir (opcional).
    :return: Lista limpia de opciones.
    """
    
    cleaned_options = [option.strip() for option in options if option.strip()]

    if exclude_options:
        exclude_options = set(exclude_options)  # Convert to set for faster lookup
        cleaned_options = [option for option in cleaned_options if option not in exclude_options]

    return cleaned_options


