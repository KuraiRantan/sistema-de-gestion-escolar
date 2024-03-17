def fields_are_valid(list_fields, dict_data):
            for field in list_fields:
                 if field not in dict_data or dict_data.get(field) is None:
                    return False
                 
            return True

def validate_data_types(types:dict, dict_data:dict):
      for type_name, type_value in types.items():
            value_data = dict_data.get(type_name, None)
            
            if value_data is None: continue
            
            if isinstance(type_value, list):
                  if value_data not in type_value:
                        return False
            elif not isinstance(value_data, type_value):
                  return False
      return True
