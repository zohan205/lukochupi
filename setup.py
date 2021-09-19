#!/usr/bin/env python
from setuptools import setup
from __version__ import VERSION

required = [
  'base64', 'random'
]

setup(
  name = "lukochupi",
  version = VERSION,
  description = "A simple password generator with various encryption methods.",
  author = "Zohan",
  url = "https://github.com/zohan205/lukochupi",
  requires = required,
)
