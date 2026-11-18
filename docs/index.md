---
icon: material/run-fast
title: Quickstart
description: Getting started quickly with Pieforhead
---

![Pieforhead Logo](images/logo.png){ align=right }

Pieforhead is a python library to help you interact with the PieFed API. It acts as a wrapper for the API that can be used in either a synchronous or asynchronous way.

Quick links:

- [Source repository](https://github.com/wjs018/pieforhead)
- [Pieforhead Examples](examples/index.md)
- PieFed API reference: [stable](https://stable.wjs018.xyz/api/alpha/swagger), [development](https://piefed.wjs018.xyz/api/alpha/swagger)
- [PieFed repository](https://codeberg.org/rimu/pyfedi)

## Installation

Installation can be done with `pip`. It's recommended that some kind of python environment is used for your project as a best practice. Some environment managers include `venv`, `uv`, and `conda`.

```bash
pip install pieforhead
```

Dependencies:

- `python` >= 3.11
- `httpx`
- `semver`
- [Optional] `pytest` - to run tests
- [Optional] `zensical` - to build docs
- [Optional] `mkdocstrings[python]` - to help build docs

## Next Steps

To help take your first steps with Pieforhead, check out the resources below:

- [Design Philosophy](philosophy.md)
- [Examples](examples/index.md)
- [API Reference](reference/pieforhead)
