#!/usr/bin/env python3


import argparse
import msgpack
import socket

# parse arguments where firest is path to the socket file
parser = argparse.ArgumentParser()
parser.add_argument("socketfile", help="socket file")
args = parser.parse_args()


# init unix socket listener/server
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.bind(args.socketfile)
sock.listen(1)


while True:
    # receive connection
    conn, addr = sock.accept()

    # init msgpack
    unpacker = msgpack.Unpacker()
    packer = msgpack.Packer()

    # read data
    while True:
        unpacker.feed(conn.recv(1))

        # parse incoming frames
        for frame in unpacker:
            # do something with frame
            frame["status"] = frame["camera"]["name"]
            for item in frame["items"]:
                item["state"] = "pass"

            # write response
            conn.send(packer.pack(frame))
