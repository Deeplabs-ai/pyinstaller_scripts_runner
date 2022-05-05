# Compiled Python Code runner
### Run python scripts with a pyinstaller-compiled python interpreter

Marco Sanguineti, Klajdi Beqiraj

---
This project allows you to perform a number of generic operations written in Python code in compiled version (C) with PyInstaller, without the need to run the setup of interpreter and virtual environment for the end user.

## How it works

It's necessary to setup a virtual environment to generate the compiled code. It's necessary to install PyInsaller:
    
    (venv) pip install pyinstaller

and every other library we'll need for the final code execution.

- In the current state it is possible to execute a chain of operations, sequentially. 
- It's not possible to pass signals or data from an operation to another (TODO)
- It's not possible to pass arguments to functions or classes (TODO)
- It's necessary to insert all the desired scripts inside the folder "scripts"
- It's necessary to compile "spec.json" following some simple rules:
  - This dictionary contains a sequence of operations, executed **sequentially**.
  - Every operation is a dictionary. The key **name** has to be bounded with the script name (relative path from "scripts") and the key **funcs** must be bounded with the list of operations to be executed from the script reported at the key **name**
- We can debug the code (before compiling) running main.py from our virtual environment
- The working path it's at the same level of the final executable file
- All the libraries must be imported inside __ main __.py or must be added to hidden_imports inside main.spec. Othewise they will not be added to available libraries, leading to a crash in the executed code
- We can compile the code with "no console" setting console=False inside main.spec. The cosole helps debugging, but might lead to errors when running scripts in batch mode.

## Compiling
If already existing, delete **build** and **dist** folders from the actual working path (../pysintaller_scripts_runner)

From cli:

    (venv) cd ../pyinstaller_scripts_runner
    (venv) pyinstaller_scripts_runner: pyinstaller main.spec

## Test your compiled code

- Open the new dist folder: you'll find a 'main' folder
- Inside 'main' you'd find all the compiled scripts and libraries and the main executable scripts (.exe on a Windows machine)
- Run your 'main' executable from CLI or doubleclicking on it
- Check the log inside the shell to asses a correct execution (we can discard all the log related to the compiler)

## 1. Hello world
Introductory example. This basic example run a sequence of operations and write an hello.txt script.

1. Copy all the scripts from example_scripts to scripts
2. Compile the project
3. From dist folder => main => run main (main.exe on Windows machine)
4. Check the new hello.txt script. It might contain the following lines:


    OK CLIENT
    goodbye
    goodbye again!!
    welcome