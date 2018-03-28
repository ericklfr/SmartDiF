import json
import sys

def generator():
    data = {
        'name': sys.argv[1],
        'virtualization': sys.argv[2],
        'type': sys.argv[3],
        'mapping_url': sys.argv[4],
 	'mapping_dir': sys.argv[5],
        'endpoint': sys.argv[6],
        'port':sys.argv[7],
        'finish': sys.argv[8],
    }

    with open('settings.json', 'w') as outfile:
        json.dump(data, outfile)

if __name__ == "__main__":
    generator()
