# Ansible_YAML_Refactor
Cleans up Ansible YAML Files. Mass removes debugs.
## Requirements:

1. [argparse](https://pypi.org/project/argparse/) 
2. [yaml](https://pypi.org/project/PyYAML/)
3. sys

## Example:

`python code_refactor.py -i testcode.yml -e 'debug 1'
`
## Future Improvements:
- Check if `debugs:` exist in Yaml doc, if not, exit

### Updates:
7/22/2020 - Added new argparse features to accept '-i' and '-e' switches. '-e' is optional as this is the exclusionary variable.

7/22/2020 - Added the abililty to add keyword exclusions, so if you want to keep a specific debug in your code, it will have to contain a values match.
