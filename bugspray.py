import argparse
from ruamel import yaml
import sys


def yaml_load(path):
    with open(path) as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print (exc)
        
    return data


def parse_data(data, exclusion):
    new = []

    for dictionary in data:

        if exclusion in dictionary.values() and 'block' not in dictionary:
            new.append(dictionary)
        if 'debug' in dictionary and 'block' not in dictionary:
            continue
        if 'block' in dictionary:
            dictionary['block'] = parse_data(dictionary['block'], exclusion)
            new.append(dictionary)
        else:
            new.append(dictionary)

    return new

def generate_yaml(path, write_data):
    # dump the yaml to the file
    with open(path, 'w') as f:
        yaml.round_trip_dump(write_data, f, allow_unicode=True, default_flow_style=False)

    # add newline before each chunk
    with open(path, 'r') as x:
        content = x.readlines()
        array = []
        for i in content:
            if '- name' in i:
                line = '\n' + i
                array.append(line)
            else:
                array.append(i)
        x.close()
    
    # write new structured output
    with open(path, 'w') as y:
        write_str = ''.join([str(i) for i in array])
        y.seek(0)   # start curser at the beginning of the file to overwrite
        y.write(write_str)            
             

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='This program will remove all debug or exclude a keyword debug')
    
    parser.add_argument('-i', action='store', dest='path', help='Stores the path to the yaml code')
    parser.add_argument('-e', action='store', dest='exclusion', help='Stores the keyword to exclude from deletion')

    result = parser.parse_args()
                        
    #path = result.path
    path = 'testcode.yml'
    exclusion = result.exclusion
                        
    if (path.endswith('.yml') or path.endswith('.yaml')):
        data = yaml_load(path)
        write_data = parse_data(data, exclusion)
        new_file = generate_yaml(path, write_data)

        print ('Successfully Refactored', path)
    else:
        print ('Invalid extension type')
        exit(0)