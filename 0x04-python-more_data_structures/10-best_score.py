#!/usr/bin/python3

def best_score(my_dict):
    if my_dict:
        return None
    else:
        max_v = None
        max_k = None
        for k, v in my_dict.items():
            if max_v is None or v > max_v:
                max_v = v
                max_k = k
        return max_k
