from typing import Dict, List

def fields_are_valid(list_fields: List[str], dict_data: Dict):
    """Validate if required fields are present in the data dictionary.

    Args:
        list_fields (List[str]): List of required fields.
        dict_data (Dict): Dictionary containing the data to be validated.

    Returns:
        bool: True if all required fields are present and not None, False otherwise.
    """
    for field in list_fields:
        if field not in dict_data or dict_data.get(field) is None:
            return False     
    return True

def validate_data_types(types: Dict, dict_data: Dict):
    """Validate if data types match the expected types defined in the types dictionary.

    Args:
        types (Dict): Dictionary containing the expected data types for each field.
        dict_data (Dict): Dictionary containing the data to be validated.

    Returns:
        bool: True if all data types match the expected types, False otherwise.
    """
    for type_name, type_value in types.items():
        value_data = dict_data.get(type_name, None)   
        if value_data is None: 
            continue
        if isinstance(type_value, list):
            if value_data not in type_value:
                raise SystemError(f'value {value_data} not in {type_value}')
                return False
        elif not isinstance(value_data, type_value):
            raise SystemError(f'instance {value_data} not is {type_value} -> {isinstance(value_data, type_value)}')
            return False
    return True
