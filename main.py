from nightlight import nightlight

def ech(a):
    return a
order = [
        #("pr", ech, "c"),
        ("nightlight", nightlight.is_redshift_enabled_clean, {"enabled": "luz nocturna", "disabled": "NO_ME_RENDERICES"}), 
        ("__i3status", "", ""),
        ]

import sys
import json

def print_line(message):
    """ Non-buffered printing to stdout. """
    sys.stdout.write(message + '\n')
    sys.stdout.flush()

def read_line():
    """ Interrupted respecting reader for stdin. """
    # try reading a line, removing any extra whitespace
    try:
        line = sys.stdin.readline().strip()
        # i3status sends EOF, or an empty line
        if not line:
            sys.exit(3)
        return line
    # exit on ctrl-c
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    print_line(read_line())
    print_line(read_line())

    while True:
        line, prefix = read_line(), ''
        if line.startswith(','):
            line, prefix = line[1:], ','

        j = json.loads(line)

        new_order = []
        for name, mod, args in order:
            if name == "__i3status":
                new_order += j
            else:
                res = mod(args)
                if res == "NO_ME_RENDERICES":
                    continue
                new_order.append({"full_text": res, "name": name})
        
        print_line(prefix+json.dumps(new_order))
