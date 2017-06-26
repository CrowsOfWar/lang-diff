
from app import *
import json

def test(expected, actual):
    if expected != actual:
        raise Exception('Test expected "' + str(expected) + '" but got "' + str(actual) + '"')

test('a5.0', find_dev_branch(json.loads('[{"name":"a4.0"},{"name":"a5.0"}]')))
test('a5.0', find_dev_branch(json.loads('[{"name":"a4.1"},{"name":"a5.0"}]')))
test('a4.1', find_dev_branch(json.loads('[{"name":"a4.0"},{"name":"a4.1"}]')))
test('b1.0', find_dev_branch(json.loads('[{"name":"a4.0"},{"name":"b1.0"}]')))
test('a1.0', find_dev_branch(json.loads('[{"name":"a1.0"},{"name":"abcd"}]')))
test('a1.0', find_dev_branch(json.loads('[{"name":"a1.0"},{"name":"bbcd"}]')))
