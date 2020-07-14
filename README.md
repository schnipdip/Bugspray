# Ansible_YAML_Refactor
Cleans up Ansible YAML Files. Mass removes debugs.

## Example:

`python code_refactor.py testcode.yml
`
## Future Improvements:
- Check if `debugs:` exist in Yaml doc, if not, exit
- Task chunk checks instead of line-by-line state check - removes the task chunk if `debug:` exists and not just a line that contains 'debug'
