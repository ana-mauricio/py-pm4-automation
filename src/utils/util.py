#!/usr/local/bin/python3
""" Module to contain helper functions that cut down on redundant code in main calls.
"""
#!/usr/local/bin/python3
""" Module to contain helper functions that cut down on redundant code in main calls.
"""
from os import getenv
import random
import string
from contextlib import redirect_stdout
from io import StringIO
import re

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
    Methods:
        run_test:
            Used in every test file to run tests and format results into
                {"results": "", "message": ""} output.
                "results" may be SUCCESS or FAIL.
                "message" may be test_output, which contains the Python unittest
                    output redirected into a buffer, or log[-1], which contains
                    the last custom log message appended during a test.
        parse_results:
            Used to transform test_output into a SUCCESS / FAIL result.
        parse_log_error:
            Used to search an html page source for 'ERROR' and capture the 'ERROR'
                message. Useful for login.
        parse_log_warning:
            Used to search an html page source for 'WARNING' and capture the 'WARNING'
                message. Useful for login.
        generate_long_text:
            Used to generate a random string of text 95 characters long.
        generate_text:
            Used to generate a random string of text 10 characters long.
        generate_email:
            Used to generate a randome email address.
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def parse_results(buffer):
    ''' Function to parse the unittest results into PM4-friendly format.
    '''
    if not buffer or buffer is '':
        return 'No unittest result detected'

    if buffer.startswith('.'):
        return 'SUCCESS'
    elif buffer.startswith('F') or buffer.startswith('E'):
        return 'FAIL'

def parse_log_error(log_message):
    ''' Function to capture ERROR message.
    '''
    return 'ERROR: ' + re.search(r'(?<=ERROR<\/strong>:\s)([^<]+)', log_message).group(0)

def parse_log_warning(log_message):
    ''' Function to capture WARNING message.
    '''
    return 'WARNING: ' + re.search(r'(?<=WARNING<\/strong>:\s)([^<]+)', log_message).group(0)

def generate_long_text():
    ''' Function to generate a random string 95 chars long. '''
    return ''.join(random.choice(string.ascii_letters) for n in range(95))

def generate_text():
    ''' Function to generate a random string 10 chars long. '''
    return ''.join(random.choice(string.ascii_letters) for n in range(10))

def generate_email():
    ''' Function to generate a random email. '''
    return ''.join(random.choice(string.ascii_letters) for n in range(10)) +\
        '@' + ''.join(random.choice(string.ascii_letters) for n in range(5)) +\
        '.' + ''.join(random.choice(string.ascii_letters) for n in range(5))

def generate_text_with_special_char():
    ''' Function to generate a random string 10 chars long with special character. '''
    return  ''.join(random.choice(string.punctuation) for n in range(10))

def generate_phone():
    ''' Function to generate a random phone with XXX-XXX-XXX format. '''
    first = str(random.randint(100,999))
    second = str(random.randint(1,888)).zfill(3)

    last = (str(random.randint(1,9998)).zfill(4))
    while last in ['1111','2222','3333','4444','5555','6666','7777','8888']:
        last = (str(random.randint(1,9998)).zfill(4))
    return '{}-{}-{}'.format(first,second, last)

