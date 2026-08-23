def flatten(d, sep='_'):
    out = {}
    for k, v in d.items():
        if isinstance(v, dict):
            for sub_k, sub_v in flatten(v, sep).items(): out[f'{k}{sep}{sub_k}'] = sub_v
        else: out[k] = v
    return out
