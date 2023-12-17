<!-- TABLE OF CONTENTS -->
<div style="display:flex;">
<details>
  <summary><strong>Table of Contents</strong></summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#project-description">Project Description</a></li>
        <li><a href="#key-components-and-modules">Key Components and Modules</a></li>
        <li><a href="#built-with">Build With</a></li>
      </ul>
    </li>
    <li><a href="#getting-start">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#pattern-documentation">Pattern Docs</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <li><a href="#license">License</a></li>
    <!-- <li><a href="#contact">Contact</a></li> -->
    <li><a href="#author">Author</a></li>
  </ol>
</details>
<img src="https://media.tenor.com/E5EdvP2EmTYAAAAi/click-mouse.gif"
    width=20 height=20
    style="transform:translate(10px, 2px) rotate(-50deg);"
>
</div>
<br>

Razor Automator
============


The RazorType General Automation System is a comprehensive solution designed for efficient task automation using a JSON template pattern. Developed with a keen focus on software design and architecture principles, the software aims to provide flexibility, maintainability, and scalability.

The selection of RazorType was driven by the necessity for a sophisticated automation system employing a JSON template pattern. Authored by [Your Name], the program is tailored to offer a comprehensive solution with an architectural approach that encourages adaptability.


<!-- ABOUT THE PROJECT -->
About The Project
============

Welcome to the RazorAutomator repository! This project is the result of the term project for the Software Design and Architecture course. Its purpose is to automate any action that conforms to a predefined pattern in the "_patterns.json_" file. With just a little push, everything can be automated!

### Project Description

The project is designed to generate structural information based on a given JSON pattern. It collects data from JSON files and creates executable code for future actions. The project primarily automates processes by utilizing system information and tools such as keyboard, mouse, and screen. As it is a console application, a user menu is created to select and execute predefined patterns. In the event of a stop request, a thread is utilized to execute functionalities.

# Software Design and Architecture

The architecture of **RazorAutomator** aligns with industry best practices and the principles emphasized in the Software Design and Architecture course. The project follows a [mention the architectural type, e.g., MVC, Microservices, etc.] architecture, dividing it into several key components and modules that contribute to its overall functionality. The chosen architecture is designed to [mention any specific goals or principles driving the software design].

### Key Components and Modules

The project consists of several key components and modules, each serving a specific purpose in the automation process. These components include:

- **Pattern Generator**: Responsible for interpreting the patterns defined in the "_patterns.json_" file. It generates executable code based on the provided structural information, allowing the automation of diverse actions.

- **Automation Tool**: This module encompasses functionalities for interacting with system elements such as the keyboard, mouse, and screen. It provides a set of basic and complex automations that can be utilized in the defined patterns.

- **Process Handler**: Manages the execution flow of the automated processes. It handles the initiation and termination of actions, responding to user commands effectively. The module employs multithreading to ensure seamless execution even during stop requests.

- **User Interface (Console Menu)**: Facilitates user interaction by providing a console-based menu. Users can select and execute predefined patterns through an intuitive interface. The console menu is an essential part of ensuring user-friendly interaction with the automation system.
> Console Menu will be replaced with the UI Menu in future releases
### Built With

This project utilizes various technologies and frameworks to ensure efficient development and a seamless user experience. Some of the major tools include:

- **Python**: The project is developed using Python, a versatile and powerful programming language.

- **PyAutoGUI**: PyAutoGUI is employed for automating mouse and keyboard actions. Here's an example of using PyAutoGUI to move the cursor to the center of the screen:

    ```python
    import pyautogui

    # Move the cursor to the center of the screen
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth // 2, screenHeight // 2)
    ```

- **Logging**: The project uses Python's built-in logging module for logging messages. It supports logging to the console and a file. Here's an example of creating a logger and logging an informational message:

    ```python
    import logging

    logger = logging.getLogger(__name__)

    # Log an informational message
    logger.info('This is an informational message.')
    ```

- **JSON Handling**: JSON files are utilized for storing configuration and pattern data. The `DataReader` class reads JSON files, and here's an example of reading a JSON file:

    ```python
    from common.ConfigHandler.reader import DataReader

    # Read a JSON file
    json_data = DataReader.read_json('path/to/your/file.json')
    ```

- **Docker**: Docker is used to containerize the application. Below is a simplified Dockerfile example for a Python application:

    ```Dockerfile
    FROM ubuntu:latest

    WORKDIR /app

    COPY ./pattern_macro /app/pattern_macro

    RUN apt-get update -y && \
        apt-get install -y python3 python3-pip

    COPY ./pattern_macro/requirements.txt /app/pattern_macro/requirements.txt
    RUN pip3 install -r /app/pattern_macro/requirements.txt

    CMD ["python3", "/app/pattern_macro/app.py"]
    ```

<br>

[Table of Content 🔺](#)

Getting Start
============

Now, it is time to get your hands dirty! This section will guide you through setting up the project and running it on your local machine.

## Prerequisites
Before you begin, ensure you have the following prerequisites installed on your machine:

- [Docker](https://www.docker.com/)

## Installation
Follow these steps to install and run RazorAutomator:

1. **Run the program using Docker:**
   - Clone the RazorAutomator repository to your local machine.
     ```bash
     git clone https://github.com/Razortype/razor-automator.git
     cd RazorAutomator
     ```
   - Build the Docker image:
     ```bash
     docker build -t razorautomator-image .
     ```
   - Run the Docker container:
     ```bash
     docker run -it razorautomator-image
     ```
2. **Create custom patterns:**
    - Read the documentation and functionalities of automator
    - Implement pattern with its custom name
    ```json
    {
        "sword_clicker": {
            "path": {
                "1": {"func": "move_cursor_to_mid"},
                "2": {
                    "func": "click", 
                    "kwargs": {"clicks": 1},
                    "times": 1}
            },
            "times": "inf"
        },
        ..
    }
    ```

That's it! You've successfully set up and initiate first pattern to RazorAutomator .run RazorAutomator on your machine.

<br>

[Table of Content 🔺](#)

Pattern Documentation
============

## Class: PatternGenerator

The `PatternGenerator` class is responsible for managing and generating patterns based on the given context. It contains the following functionalities:

### Method: enter_patterns

- **Description:** Enters and processes patterns into the system.
- **Parameters:**
  - `patterns`: A dictionary containing pattern names and their contexts.

### Method: generate_pattern

- **Description:** Generates a pattern with specified name and context.
- **Parameters:**
  - `pattern_name`: Name of the pattern.
  - `context`: Context information for the pattern.

### Method: generate_piece

- **Description:** Generates a pattern piece with specified index and context.
- **Parameters:**
  - `index`: Index of the piece.
  - `piece_context`: Context information for the piece.

### Method: get_registered

- **Description:** Retrieves a list of registered patterns.
- **Returns:** A list of tuples containing human-readable pattern names and pattern names.

### Method: get_pattern

- **Description:** Retrieves a specific pattern by name.
- **Parameters:**
  - `pattern_name`: Name of the pattern.
- **Returns:** The pattern object.

## Class: PatternPiece

The `PatternPiece` class represents a single piece of a pattern. It contains the following functionalities:

- **Method: execute**
  - **Description:** Executes the defined function for the specified number of times.
  - **Parameters:** None

## Class: Pattern

The `Pattern` class represents a complete pattern with multiple pieces. It contains the following functionalities:

### Method: start

- **Description:** Initiates the execution of the pattern.
- **Parameters:** None

### Method: execute_all

- **Description:** Executes all pieces of the pattern.
- **Parameters:** None

- **Attributes:**
  - `pattern_name`: Name of the pattern.
  - `times`: Number of times the pattern should be executed.
  - `pieces`: List of `PatternPiece` objects.
  - `running`: Flag indicating if the pattern is currently running.

<br>

[Table of Content 🔺](#)

License
============

MIT License

Copyright (c) 2023 Orkun Kurul

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Author
============

<!-- PROJECT AUTHOR -->
<br />
<div align="center"
style = "display:flex; flex-direction:column; align-items:center;">
    <div style="float: left;
  margin-top: 20px;
  width: 200px;
  height: 200px;
  border-radius: 100%;
  overflow: hidden;">
        <a href="https://github.com/Razortype">
            <img src="https://avatars.githubusercontent.com/u/55176611?v=4" width=200 height=200 alt="Logo">
        </a>
    </div>
    <br>
    <div>

  <h3 align="center">Orkun Kurul <br> (Razortype) </h3>

  <p align="center">
    Web and Automation Project Developer
    <br />
    <a href="https://github.com/Razortype"><strong>Explore my profile »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Razortype/razor-automator">View Demo</a>
    ·
    <a href="https://github.com/Razortype/razor-automator/issues">Report Bug</a>
    ·
    <a href="https://github.com/Razortype/razor-automator/issues">Request Feature</a>
  </p>
    </div>
</div>

<br>

[Table of Content 🔺](#)