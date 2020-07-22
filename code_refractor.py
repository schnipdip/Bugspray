import argparse
import yaml
import sys

def yaml_load(path):
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    
    return data


def parse_data(data, exclusion):
    new = []
    blank = []
    counter = 0
    
    for i in data:
        if exclusion in i.values():
            print (i)
            new.append(i)
        if 'debug' not in i.keys() and 'block' not in i.keys():
            '''Locates the Debug: tags'''
            new.append(i)
        if 'block' in i.keys():
            blank.append(i)

            for x in blank:
                if 'debug' in x['block'][counter]:
                    del x['block'][counter]  
                    new.append(x)
                    counter += 1
                                  
    return (new)

def generate_yaml(path, write_data):
    with open(path, 'w') as f:
        yaml.dump(write_data, f, sort_keys=False)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='This program will remove all debug or exclude a keyword debug')
    
    parser.add_argument('-i', action='store', dest='path', help='Stores the path to the yaml code')
    parser.add_argument('-e', action='store', dest='exclusion', help='Stores the keyword to exclude from deletion')

    result = parser.parse_args()
                        
    path = result.path
    exclusion = result.exclusion
                        
    if (path.endswith('.yml') or path.endswith('.yaml')):
        data = yaml_load(path)
        write_data = parse_data(data, exclusion)
        new_file = generate_yaml(path, write_data)

        print ('Successfully Refactored', path)
    else:
        print ('Invalid extension type')
        exit(0)
