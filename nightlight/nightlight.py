from sys import argv
import subprocess


def is_redshift_enabled_clean(fmt):
    is_redshift_on, _ = is_toggled()
    if is_redshift_on:
        return fmt.get("enabled", "luz nocturna encendida")
    else:
        return fmt.get("disabled", "luz nocturnan't")

def is_toggled():
    from os.path import join
    from pathlib import Path
    file_path = Path(__file__).parent.resolve()
    file_path = join(file_path, "toggled")
    
    with open(file_path, "r")  as f:
        is_it = f.read()
        return (True if is_it == "true" else False, file_path)
        
def toggle():
    is_it, file_path = is_toggled()
    with open(file_path, "w") as toggled_file:
        if is_it:
            subprocess.run(["redshift", "-x"])
            toggled_file.write("false")
        else:
            subprocess.run(["redshift", "-O", "4500K", "-r", "-P"])
            toggled_file.write("true")

def text():
    print(is_toggled())
    pass

if __name__ == "__main__":
    assert len(argv) > 1 
    if argv[1] == "toggle":
        toggle()
    else:
        text()
