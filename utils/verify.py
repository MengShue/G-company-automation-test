import requests
import re


def verify_status_code(res, expected_status_code):
    assert isinstance(res, requests.Response), "Not Response type"
    assert res.status_code == int(expected_status_code), "status_code NOT as  expected"


def verify_content_value(value, expected_content):
    assert type(value) == type(expected_content)
    assert value == expected_content, "expected content NOT as expected"


def verify_content_value_regex(value, expected_content):
    assert isinstance(value, str)
    pattern = re.compile(expected_content, re.UNICODE)
    assert pattern.match(value) is not None, "expected REGEX content NOT as expected"


def verify_key_exist(res, key):
    assert key in res, "expected key existence NOT as expected"


def verify_list_length(list_data, expected_count):
    assert isinstance(list_data, list)
    assert len(list_data) == expected_count, "expected length of list NOT as expected"
