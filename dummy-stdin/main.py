#!/usr/bin/env python3


import sys
import json
import traceback


while True:
    try:
        # read stdin
        line = sys.stdin.readline()
        if len(line) < 3:
            continue

        # parse
        frame = json.loads(line)

        # do something with frame:
        frame["status"] = "Dummy block"
        for item in frame["items"]:
            item["state"] = "pass"

        # write response to stdout
        sys.stdout.write(json.dumps(frame))
        sys.stdout.write("\n")
        sys.stdout.flush()
    except Exception as e:
        with open("errors.log", "a") as f:
            f.write(str(e))
            f.write(traceback.format_exc())
