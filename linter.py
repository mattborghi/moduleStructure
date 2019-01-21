"""
In order to use this script call it:
$ python linter.py [dir=SCR] [OPT]

[SCR] is the source folder where the output will be stored.
By default it will be ".style".

[OPT] are the optional paramters which tells which command will be run
 OPT: --Command1, which tells that command1 will be run. By default it will be false.
 Available list of commands:
    - flake8
    - black
    - pylint
    - pyflakes
    - pydocstyle

Example
-------
1. $ python linter.py: will not run anything.
2. $ python linter.py --flake8 ".style": run flake8 and store the ouput in the .style folder.
"""
import sys
import os
from termcolor import colored


class Syntax:
    def display_files(self, dir_location, decision_dict):
        index = 1
        for root, dirs, files in os.walk(dir_location):
            for filename in files:
                decision_dict[str(index)] = filename
                print("\n" + str(index) + ". " + filename)
                index += 1
        decision_dict[str(index)] = "Exit"
        print("\n" + str(index) + ". " + "EXIT")
        return decision_dict

    def generateORload(self, dir_location):
        while True:
            decision_dict = {}
            print(colored("\nWhich files do you want to inspect: \n", "green"))
            decision_dict = self.display_files(dir_location, decision_dict)
            # print(decision_dict)
            decision = input("\nSelect option: ")
            try:
                decision = decision_dict[str(decision)]
            except ValueError:
                print("\nInput must be an integer.")
                continue
            except KeyError:
                print("\nValue is not right.")
                continue
            if decision == list(decision_dict.values())[-1]:
                sys.tracebacklimit = 0
                print("\nNo more files to show.")
                break
            elif decision not in decision_dict.values():
                print("\nMust choose between 1,2 or 3!.")
            else:
                # Load file and output
                print("Chosen file is: " + decision)
                with open(dir_location + "/" + decision) as f:
                    for line in f:
                        print(line.strip())


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 1:
        # No exit parameters, exit
        print("No arguments passed.. exiting!")
        sys.tracebacklimit = 0
        exit()
    # Get the parameters bar the first one (which is the script name)
    lista = sys.argv[1:]
    # Is a folder given?
    try:
        dir_location = [
            lista[index] for index in range(len(lista)) if "dir=" in lista[index]
        ][0]
        # remove the location from the list
        lista.remove(dir_location)
        # just keep the directory
        dir_location = dir_location[4:]
    except IndexError:
        print("Location set as default dir = '.style' ")
        dir_location = ".style"
    # From the rest, which commands should I run?
    # Loop over the commands and store them in an array
    print("Lista is of length: " + str(len(lista)))
    print("Location directory: " + dir_location)
    commands = [elem[2:] for elem in lista]
    print("commands: [%s]" % ",".join(map(str, commands)))
    to_run = []
    for elem in commands:
        if elem == "flake8":
            to_run.append("flake8 --filename=*.py >> " + dir_location + "/flake8.txt")
        elif elem == "black":
            to_run.append(
                "black --check --diff . >> " + dir_location + "/black_diff.txt"
            )
            to_run.append("black . >> " + dir_location + "/black_res.txt")
        elif elem == "pylint":
            to_run.append("pylint TestProject >> " + dir_location + "/pylint.txt")
        elif elem == "pyflakes":
            to_run.append("pyflakes TestProject >> " + dir_location + "/pyflakes.txt")
        elif elem == "pydocstyle":
            to_run.append("pydocstyle . >> " + dir_location + "/pydocstyle.txt")
        else:
            print("There was a problem with an input command parameter: " + elem)
            exit()
    # Run the commands and store its output
    print("Creating directory " + dir_location)
    os.system("mkdir " + dir_location)
    for elem in to_run:
        print("Running command: " + elem)
        os.system(elem)
    # Which ones do you want to see? Do this until we want to exit
    a = Syntax()
    a.generateORload(dir_location)
    # Delete the new created folder
    print("Removing folder " + dir_location)
    os.system("rmdir /S /Q " + dir_location)
