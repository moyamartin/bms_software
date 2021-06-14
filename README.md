# BMS debug tool

The BMS software is used as a tool for debugging and visualize the current
status of the device, it is based on 
[python3.7](https://www.python.org/downloads/) and a few modules installed by
pip.

# Installation

## Linux

To install this tool you only need to run the `setup.sh` script, this will
install `python3.7`, `pip` and all the required dependencies and as well
generate a virtual environment.

```
./setup.sh
```

And to run it, before you have to activate the virtual environment (venv) and
then run the tool.

```
source venv/bin/activate
python bms_debug_tool.py
```
