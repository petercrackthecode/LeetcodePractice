"""
You're given a URL string of the following format:

Copy code
"https://www.example.com/page?param1=value1&param2=value2&param3=value3"
Your task is to write a function that takes such a URL string as input and returns a dictionary (or a similar key-value data structure in your programming language of choice) where each query parameter is a key and its corresponding value is the value.

Example:

Input:

"https://www.example.com/page?param1=value1&param2=value2&param3=value3"
Output:

json
Copy code
{
  "param1": "value1",
  "param2": "value2",
  "param3": "value3"
}
Consider the following:

The URL will always be well-formed and will follow the standard scheme as shown in the example.
You can assume that each parameter in the query string will have a unique key.
Parameter values are always strings.
If the URL does not have parameters, your function should return an empty dictionary.
This problem tests your ability to manipulate strings, understand data structures, and handle edge cases. 
It's representative of the practical, real-world problems that might be encountered in a Stripe technical interview, 
focusing on parsing and handling web data.
"""

from typing import Dict, List


def parse_parameters(url: str) -> Dict[str, str]:
    if not "?" in url:
        return dict()

    ans: Dict[str, str] = dict()

    params_str: str = url.split("?")[1]
    if params_str.strip() == "":
        return dict()

    param_val_strs: List[str] = params_str.split("&")

    for param_val_str in param_val_strs:
        param, val = param_val_str.split("=")
        ans[param] = val

    return ans


# url: str = "https://www.example.com/page?param1=value1&param2=value2&param3=value3"

url: str = "facebook.com/page?"
ans = parse_parameters(url)

print(f"ans = {ans}")
