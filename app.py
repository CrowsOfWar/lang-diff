
from diff import gen_diff
import urllib.request
import json

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def find_dev_branch(branches):
    develop_branch = ''
    develop_version = 0

    for i in range(0, len(branches)):
        branch = branches[i]
        branch_name = branch['name']
        if branch_name.startswith(('a', 'b', 'i')) and isFloat(branch_name[1:]):

            branch_version = float(branch_name[1:])
            if (branch_name.startswith('b')):
                branch_version += 100

            if branch_version > develop_version:
                develop_branch = branch_name
                develop_version = branch_version

    return develop_branch

base_url = 'https://api.github.com/repos/CrowsOfWar/AvatarMod/'

branches_json = urllib.request.urlopen(base_url + 'branches').read()
branches = json.loads(branches_json)
dev_branch_name = find_dev_branch(branches)

dev_branch_json = urllib.request.urlopen(base_url + 'branches/' + dev_branch_name).read()
dev_branch = json.loads(dev_branch_json)

dev_branch_date = dev_branch['commit']['commit']['author']['date']
print(dev_branch_date)
