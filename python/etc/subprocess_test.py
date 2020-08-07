import subprocess

if __name__ == '__main__' :
    #work fine python3.5 or higher
    subprocess.run(['dir'], shell=True)

    #work fine python3.5 below
    command = 'ls -al ' + ...
    result = subprocess.check_output([command], shell=True)