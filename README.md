# Building a simple CLI Tool

In this project, you will encounter and/or use the following
- Github PR Template
- Python File Handling
- Python Modules : SYS, JSON, CSV, OS(Maybe)

## Convections / Coding Styles

- Ensure you appropriately name your functions, classes and modules using the expected naming convections
- Ensure to have exactly two(2) empty lines after your imports within modules for the sake of readability
- Ensure to be consistent with usage of string quotes. Lets stick with using single quotes except in situations where double quotes are required

## Project Description

In this project, you will be building a simple command line tool for writing predefined data in python into files in the formats JSON and CSV. The data you will be writing into these files has been predefined in the `src/data.py` module. Take a look at the module to see the data in there - It is a dictionary holding details of programming languages (Note, they are fake data)

There is a `main.py` module at the root of the project which will serve as our CLI tool expected to be run on the terminal. The usage of this CLI tool on the terminal is seen and described below

```bash

Machine> python main.py <format> <keys>

```

We can see in the command above that along with attempting to execute the `main.py` module with python, we have two more arguments passed in, namely `format` and `keys`. These arguments will be used to determine what format to write data in and what data to actually write
- The `format` argument can only have one of two values, namely `json` & `csv`
- The `Keys` argument can be one or more of the keys of the dictionary defined in `src/data.py`

Note that `main.py` file is simply expected to collect arguments from the terminal and then pass/delegate actual operation to modules defined in the `src` folder. This means that you are not expected to write actual codes that perform the operation of writing to files into this module.

Upon running the command, a file named `data.json` or `data.csv` depending on format should be generated into the the current working directory with contents specified by the keys in the command.

Below are examples using the above command for writing data in JSON or CSV format

**Example #1**

```bash

Machine> python main.py json java javascript

```

After running the above command, a `data.json` file is generated into the current working directory with the below as the file content. Note that the JSON content is an array of objects

```json

[
    {
        "oop": true,
        "popularity": 7,
        "extension": "java",
    },
    {
        "oop": true,
        "popularity": 10,
        "extension": "js",
    },
]

```

**Example #2**

```bash

Machine> python main.py json php python golang

```

After running the above command, a `data.csv` file is generated into the current working directory with the below as the file content. Note how the keys of the records are used as the header for the CSV.

```text

oop,popularity,extension
true,10,php
true,9,py
false,4,go

```

## Delivery Requirements

- Create a PR template of your choice into the `.github` folder to be used for PRs you will raise later
- Complete the implementation of the project description in the below section and also, write unit tests for all your implementations `(src, tests, main.py)`
- All implementation modules should go in the `src` folder and should be well organized
- All unit test modules for your implementations should go in the `tests` folder and should be well organized too
- Only use the JSON & CSV modules that came with the python installation. Meaning don't install/use any third-party module for your JSON & CSV processing
- Do not push the following files and folders to Github by simply ignoring them in the `.gitignore` file (`__pycache__`, `data.json` and `data.csv`)
- When done and all tests are passing, raise a PR with a good title and body structured based on the content of the PR template you created at the beginning
