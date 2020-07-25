![bugspray_img](https://funkyimg.com/i/36qvF.png) ![bugspray](https://funkyimg.com/i/36qh3.png)

Bugspray cleans up Ansible YAML Files and mass removes debugs.

*This is a personal project not affiliated with the [Ansible](https://github.com/ansible/ansible) Project*

## Requirements:

1. [argparse](https://pypi.org/project/argparse/) 
2. [yaml](https://pypi.org/project/PyYAML/)
3. sys

## Installation:

`
pip install -r .\requirements.txt
`

Or to update existing packages:

`
pip install -U -r .\requirements.txt
`

## Example:

`python code_refactor.py -i testcode.yml -e 'debug 1'
`

`python code_refactor.py -h
`
## Future Improvements:
- Check if `debugs:` exist in Yaml doc, if not, exit


### Special Thanks:
- TrayKnots 
