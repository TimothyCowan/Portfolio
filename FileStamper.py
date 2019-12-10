import datetime
from os import chdir, environ, path
from platform import system
from socket import gethostname

# create or append file name given from input. Adds The date and time
# v1 - By Tim Cowan

def main():
    your_name = gethostname()
    your_time = datetime.datetime.now()
    your_file = input("Please enter a name for the file to create/append -->")  # include extension if desired

    # test for windows or other and sets cwd to users home
    if system() == "Windows":
        chdir(environ['HOMEPATH'])
    else:
        chdir(environ['HOME'])

    # previously named file is created or append
    if path.isfile(your_file):
        print('This file already exist')
        print(f'appending hostname:>{your_name}< and local time to file: >{your_file}<')
        open(your_file, 'a').write(f"\nOpened by:>{your_name}< at {your_time}")
    else:
        print('This file does not currently exist')
        print(f'writing hostname:>{your_name}< and local time to file:>{your_file}<')
        open(your_file, 'w').write(f"Created by:>{your_name}< at {your_time}")


if __name__ == "__main__":
    main()
