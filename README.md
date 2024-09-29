# FanCode Task Completion Checker

This project is a Python-based API automation solution that verifies if all users from the city **FanCode** (identified by specific latitude and longitude values) have completed more than 50% of their tasks.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [APIs Used](#apis-used)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [Configuration](#configuration)
- [How to Run Tests](#how-to-run-tests)
- [Output Example](#output-example)


## Features
- Fetches users and todos from external APIs.
- Filters users from **FanCode** city based on their latitude and longitude.
- Checks if those users have completed more than 50% of their tasks.
- Prints the results directly in the terminal.

## Project Structure
The following structure is used to keep the code organized and reusable:

├── src/ │ ├── api_client.py │ ├── user_filter.py │ ├── task_checker.py │ └── config.json ├── tests/ │ └── test_fancode_tasks.py ├── requirements.txt └── README.md



## APIs Used
The project uses mock APIs from `jsonplaceholder.typicode.com`:
- `/users`: Fetches user details.
- `/todos`: Fetches user tasks (todos).


## Prerequisites
Before running the project, make sure you have the following installed:
- Python 3.x
- `pip` (Python package installer)
  
Optionally, it’s recommended to use a virtual environment to manage dependencies

python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows


## Setup and Installation

Follow the steps below to set up and run the project on your local machine:

### 1. Clone the Repository

First, clone the repository to your local machine using the git command

### 2. Set Up a Virtual Environment

For linux/MAC , use following command : 
python3 -m venv venv
source venv/bin/activate

For Windows , use following command : 
python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies

After cloning the repository and setting up a virtual environment, install the required Python packages by running the following command:

pip install -r requirements.txt

## Configuration

The project uses a config.json file to store the base API URL. By default, the API URL is set to http://jsonplaceholder.typicode.com.

If you need to modify the API URL or other configurations, you can do so in the config.json file.

## How to Run Tests

To check the functionality and to verify if FanCode users have completed more than 50% of their tasks, run the following test using pytest:

pytest -s tests/test_fancode_tasks.py

The -s flag ensures that the print statements used in the test file will display the output in the terminal.

## Output Example

After running the tests, you should see the results directly in your terminal. The output will indicate whether the FanCode users have completed more than 50% of their tasks.

Sample Output : 

Filtered FanCode Users:
{'id': 1, 'name': 'Leanne Graham', 'address': {'geo': {'lat': '-37.3159', 'lng': '81.1496'}}}

All FanCode users have more than 50% of their tasks completed.

Or, if some users don't meet the criteria: 
Some FanCode users do not have more than 50% of their tasks completed.







