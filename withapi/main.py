#!/usr/bin/env python3


import sys
import json
import traceback
import io
from PIL import Image


import rtmipapi

api = rtmipapi.Client("http://admin:admin@127.0.0.1:8888")
log = open("errors.log", "a")


while True:
    try:
        # read stdin
        line = sys.stdin.readline()
        if len(line) < 3:
            continue

        # parse 
        frame = json.loads(line)

        # do something with frame.img
        
        # load events for the previous 30 minutes
        events = api.events(frame["camera"]["id"], frame["time"]-1800)
        for e in events:
            # get an image of each event
            imgdata = api.event_image(e.frame)
            img = Image.open(io.BytesIO(imgdata))
            # do something with img

        status = f'{len(events)} events'


        # write response to stdout
        sys.stdout.write(json.dumps({"status":status}))
        sys.stdout.write("\n")
        sys.stdout.flush()

    except Exception as e:
        log.write(str(e))
        log.write(traceback.format_exc())
