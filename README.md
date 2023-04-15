# OpenClassroom - Python Developer Path

**Project 7:** Solve Problems Using Algorithms in Python

**Student:** Abdoul Baki Seydou

**Date:** 04/04/2023

# Abstract
This project consists of designing for a client, AlgoInvest&Trade, 
an algorithm that will maximize their clients’ profits after two years of investment, 
an algorithm capable of trying out all the different combinations of shares that fit their constraints, 
and choose the most profit-yielding shares to buy. 

# Requirement

Latest version of Python must be installed.

You can download the latest version for your system from : https://www.python.org/downloads/

# Installation

The following commands rely on the knowledge of how to use the terminal (Unix, macOS) or the command line (Windows).

**1 - Get the code**

  * $ git clone https://github.com/Afudu/P7_OpenClassroom.git

**2 - Move to the folder**

  * Unix/macOS/Windows: cd P7_OpenClassroom

**3 - Create a virtual environment**

  * Unix/macOS: $ python3 -m venv pythonenv
  * Windows: py -m venv pythonenv
  
    * Note: you can create the virtual environment in another folder, then move to that folder to run the command above.
    * Example: in the above command, our virtual environment created is called pythonenv - you can give a different name.

**4 - Activate the virtual environment created**

  * Unix/macOS: $ source pythonenv/bin/activate

  * Windows: pythonenv\Scripts\activate

**5 - Securely upgrade pip**

 * Unix/macOS/Windows: pip install --upgrade pip

**6 - Install all dependencies**

 * Unix/macOS/Windows: pip install -r requirements.txt

# Running the application

To run each of the four scripts, in the terminal (Unix, macOS) or command line (Windows):

python script_file.py

# PEP 8 adherence

The folder 'flake_report' in the repository contains an HTML report generated by flake8-html which displays no errors.
A new report can be generated by running the following command in the terminal (Unix, macOS) 
or command line (Windows): flake8

The file setup.cfg in the root of the repository contains the settings used to generate the report.