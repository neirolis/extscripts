# Examples of extscripts

External custom scripts are designed to create blocks of analytics schemes. This repository contains examples of dummy blocks.

Each `extscript` must contain a `manifest.json` file, some icon image, and in the case of `stdin` or `unixsocket` types executable file.

To add a `extscript` to RTMIP, need to put it to the `extscripts` directory of `RTMIP`, ie: `/srv/rtmip/extscripts/dummy-stdin`. Where should the manifest.json, executable file and icon be.

There are 3 ways to transfer data from RTMIP to exscript: `stdin/stdout`, `unixsocket`, `http` - the `transport` field in the `manifest.json`.
And two data serialization formats: `json`, `msgpack` - the `serialize` field in the `manifest.json`.
It is possible to use these two items in any combination.

Example of manifest.json:

```json
{
  "name": "Name of block",
  "desc": "Description used as tooltip",
  "icon": "icon.png",
  "exec": "./some_executable_file",

  "transport": "stdin", // stdin, unixsocket, http
  "serialize": "json", // json, msjpack

  "variables": [
    {
      "name": "threshold",
      "label": "Threshold",
      "default": "0.5",
      "type": "number"
    },
    {
      "name": "text",
      "label": "Text"
    }
  ]
}
```

The executable file can be presented in any programming language, the main thing is that it has an executable flag. The developer should take care of installing and dependencies and libraries himself, if any are required.

The specified `variables` will be displayed on the analytics block. And passed as command-line arguments when running the executable file. For a block with `http` transport, variables will be passed as url query.

The block is launched once for each analytics, and accordingly can be used for a variety of cameras on which this analytics is used.

Errors should be written to the stderr channel, the last stderr line will be displayed as an error on the analytics block.
