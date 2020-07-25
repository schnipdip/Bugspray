![bugspray_img](https://funkyimg.com/i/36qvF.png) ![bugspray](https://funkyimg.com/i/36qh3.png)

Are you tired of having to clean up debugs when pushing development code to Ops/Production? 

Bugspray allows you to mass remove debugs from your Ansible YAML files _or_ you can selectively keep debugs in your code!

*This is a personal project not affiliated with the [Ansible](https://github.com/ansible/ansible) Project*

## Requirements:

1. [argparse](https://pypi.org/project/argparse/) 
2. [ruamel.yaml](https://pypi.org/project/ruamel.yaml/)
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

Process a single file with a exclusion:

`
python bugspray.py -i testcode.yml -e 'debug 1'
`

Process multiple files:

_Note: If using batch processing, the location of the batch.txt file needs to be located within the same directory_

`
python bugspray.py -L batch.txt
`

Get Help:
`python bugspray.py -h
`

### Special Thanks:
- TrayKnots 
