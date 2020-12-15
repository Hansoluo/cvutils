#!/bin/bash -e

rm -rf build
rm -rf dist
python3.6 setup.py sdist bdist_wheel
python3.6 -m pip install dist/*
twine upload dist/*