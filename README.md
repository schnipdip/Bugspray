[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e53981009b0b48a7b7e8efc200125af7)](https://app.codacy.com/manual/cjh30/Bugspray?utm_source=github.com&utm_medium=referral&utm_content=schnipdip/Bugspray&utm_campaign=Badge_Grade_Dashboard)
[![Known Vulnerabilities](https://snyk.io/test/github/schnipdip/Bugspray/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/schnipdip/Bugspray?targetFile=requirements.txt)


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

Process files with the No Operation flag:

`
python bugspray.py -i testcode.yml -n
`

Get Help:

`
python bugspray.py -h
`

_Video and Gifs for extra help are located in the `media/gifs` or `media/mp4` folders._

### Special Thanks:
- TrayKnots 
