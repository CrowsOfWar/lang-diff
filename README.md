Lang-Diff Readme
================

This is a simple tool to help translators know what new things to translate. It generates diffs between [AvatarMod's language files](https://github.com/CrowsOfWar/AvatarMod/blob/master/src/main/resources/assets/avatarmod/lang/en_US.lang).

Whenever you run it, the program scans for new changes in the language file since it was last run. If it finds any changes, it shows you the diff between them. Lang-diff also creates the file `_commitcache.txt` in the folder it was run, which is necessary to keep track of new changes.

Installation
------------

**On windows**

Find the releases tab, and download and run the latest .exe you can find.

**Other OS**

Find the releases tab, and download the repo at that release. Run `app.py` from the command line. It requires dateutil which can be installed by running:

> pip install python-dateutil

Further options to run will be added in the future.

How it works
------------

Lang-diff relies on the GitHub REST API.

* It first scans for a develop branch. I actually use the next version number as the name for the develop branch, so the program goes through each branch and tries to find one in the correct format. 
* It then finds the latest commit on the develop branch, which allows it to access the latest lang file on develop branch
* The latest commit when lang-diff was run before is stored in `_commitcache.txt`. It loads the lang file at that commit
* It then generates a diff between the old lang file and the new one
* It stores the latest commit in the cache
