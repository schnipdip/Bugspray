![bugspray_img](https://funkyimg.com/i/36qvF.png) ![bugspray](https://funkyimg.com/i/36qh3.png)

Are you tired of having to clean up debugs when pushing development code to Ops/Production? 

Bugspray allows you to mass remove debugs from your YAML files _or_ you can selectively keep debugs in your code!

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

- keep list formatting with ruamel.yaml

### Special Thanks:
- TrayKnots 
