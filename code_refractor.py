import yaml
import sys

def yaml_load(path):
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    
    return data


def parse_data(data):
    new = []
    blank = []
    counter = 0

    for i in data:
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

    path = sys.argv[1]

    if (path.endswith('.yml') or path.endswith('.yaml')):
        #path = 'testcode.yml'
        data = yaml_load(path)
        write_data = parse_data(data)
        new_file = generate_yaml(path, write_data)

        print ('Successfully formated', path)
    else:
        print ('Invalid extension type')
        #exit(0)

