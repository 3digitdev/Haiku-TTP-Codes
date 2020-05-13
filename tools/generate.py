"""
Generates the files in the folder structure as skeleton JSON files for each code
List taken from https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
"""
#!/usr/bin/env python3

import json
import os

from typing import List


CODES = [
    # 1XX
    "100 Continue",
    "101 Switching Protocols",
    "102 Processing",
    "103 Early Hints",
    # 2XX
    "200 OK",
    "201 Created",
    "202 Accepted",
    "203 Non-Authoritative Information",
    "204 No Content",
    "205 Reset Content",
    "206 Partial Content",
    "207 Multi-Status",
    "208 Already Reported",
    "226 IM Used",
    # 3XX
    "300 Multiple Choices",
    "301 Moved Permanently",
    "302 Found",
    "303 See Other",
    "304 Not Modified",
    "305 Use Proxy",
    "306 Switch Proxy",
    "307 Temporary Redirect",
    "308 Permanent Redirect",
    # 4XX
    "400 Bad Request",
    "401 Unauthorized",
    "402 Payment Required",
    "403 Forbidden",
    "404 Not Found",
    "405 Method Not Allowed",
    "406 Not Acceptable",
    "407 Proxy Authentication Required",
    "408 Request Timeout",
    "409 Conflict",
    "410 Gone",
    "411 Length Required",
    "412 Precondition Failed",
    "413 Payload Too Large",
    "414 URI Too Long",
    "415 Unsupported Media Type",
    "416 Range Not Satisfiable",
    "417 Expectation Failed",
    "418 I'm a teapot",
    "421 Misdirected Request",
    "422 Unprocessable Entity",
    "423 Locked",
    "424 Failed Dependency",
    "425 Too Early",
    "426 Upgrade Required",
    "428 Precondition Required",
    "429 Too Many Requests",
    "431 Request Header Fields Too Large",
    "451 Unavailable For Legal Reasons",
    # 5XX
    "500 Internal Server Error",
    "501 Not Implemented",
    "502 Bad Gateway",
    "503 Service Unavailable",
    "504 Gateway Timeout",
    "505 HTTP Version Not Supported",
    "506 Variant Also Negotiates",
    "507 Insufficient Storage",
    "508 Loop Detected",
    "510 Not Extended",
    "511 Network Authentication Required",
]

UNOFFICIAL_CODES = [
    "103 Checkpoint",
    "218 This is fine",
    "419 Page Expired",
    "420 Method Failure",
    "420 Enhance Your Calm",
    "430 Request Header Fields Too Large",
    "450 Blocked by Windows Parental Controls",
    "498 Invalid Token",
    "499 Token Required",
    "509 Bandwidth Limit Exceeded",
    "526 Invalid SSL Certificate",
    "529 Site is overloaded",
    "530 Site is frozen",
    "598 Network read timeout error"
]


def generate_code_files(code_list: List[str], base: str) -> None:
    """Generate files in folder structure"""
    for code in code_list:
        parts = code.split(' ')
        status = parts[0]
        name = " ".join(parts[1:])
        path = os.path.join('codes', base, f'{status[0]}XX', f'{status}.json')
        data = {
            'code': int(status),
            'name': name,
            'messages': []
        }
        with open(path, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)


def main():
    """main function"""
    if os.getcwd().split(os.path.sep)[-1] == 'tools':
        os.chdir('../')
    generate_code_files(CODES, base='official')
    generate_code_files(UNOFFICIAL_CODES, base='unofficial')


if __name__ == "__main__":
    main()
