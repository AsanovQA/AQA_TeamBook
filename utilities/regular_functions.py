import re


def reg_token(res_text):
    key_value_pairs = re.findall(r'(\w+)=>(.+?)(?=[,}])', res_text)
    response_dict = {key.strip(): value.strip().strip('"') for key, value in key_value_pairs}
    return response_dict.get('token')
