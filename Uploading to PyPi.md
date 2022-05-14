# Building and Uploading to PyPi

This file contains information on how to build the project and upload a new version to PyPi. First, you must open the `setup.py` file and change the version number.

Next, type this command from inside the top folder of `AerodynamicsPy`:

```
python setup.py sdist bdist_wheel
```

This build the project. To upload it to PyPi, type:

```
python -m twine upload dist/*
```
