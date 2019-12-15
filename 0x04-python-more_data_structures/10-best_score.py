#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        _max = 0
        for key, value in a_dictionary.items():
            if value > _max:
                _max = value
                name = key
        return name
                
