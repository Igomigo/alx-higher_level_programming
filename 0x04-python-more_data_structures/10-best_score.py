#!/usr/bin/python3

def best_score(my_dict):
    max_v = None
    max_k = None
    for k, v in my_dict.items():
        if max_v is None or v > max_v:
            max_v = v
            max_k = k
        else:
            return None
    return max_k