#!/usr/bin/env python
import os
import sys

sys.path.append(os.path.normpath(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../")))
sys.path.append(os.path.normpath(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../rest_api/")))

for i in sys.path:
    print i

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
