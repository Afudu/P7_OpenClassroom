# Solve Problems Using Algorithms in Python

**OpenClassrooms - Python Developer Path:** Project 7

**Student:** Abdoul Baki Seydou

**Date:** 04/04/2023 

## Table of Contents
1. [Summary](#summary)
2. [Constraints](#constraints)
3. [Technologies Used](#technologies-used)
4. [Project Tasks](#project-tasks)
5. [Local Development](#local-development)
   - [Prerequisites](#prerequisites)
   - [Setup on macOS/Linux](#setup-on-macoslinux)
   - [Setup on Windows](#setup-on-windows)
   - [Running the Application](#running-the-application)
   - [Linting](#linting)
   - [Screenshots](#screenshots)

## Summary
This project consists of designing for a client, **AlgoInvest&Trade**, 
a memory-efficient algorithm that reads the information about shares from a file, 
then suggest a list of the most profit-yielding ones within the constraints.

## Constraints
- Each share can only be bought once.
- A fraction of a share cannot be bought.
- Maximum amount to spend is: 500 euros.
This problem is known as the 01 knapsack problem.

## Technologies Used
- **Programming Languages:** Python
- **Libraries:** Csv, itertools, time.
- **Database:** Data read from text files.

## Project Tasks
We will approach the resolution of the problem in 3 parts:

- **Part1: Bruteforce solution** for a list of 20 shares, we create a brute-force solution will try out 
all the different combinations of shares then return the combination with the highest profit within the constraints.

- **Part2: Optimized solution for 20 shares** Creation of an optimized version of the brute-force solution capable of returning 
the same results for the list of 20 shares in less than one second.

- **Part3: Optimized solution for 1000 shares** We test the optimized solution on past datasets with 1000 shares and compare the results.

## Local Development

### Prerequisites
- Python 3.6 or higher.

### Setup on macOS/Linux

1. **Clone the Repository**
   ```bash
   cd /path/to/put/project/in
   git clone https://github.com/Afudu/P7_OpenClassroom.git

2. **Move to the folder**
   ```bash
   cd P7_OpenClassroom

3. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   
4. **Activate Environment**
   ```bash
   source venv/bin/activate 
   
5. **Securely upgrade pip**
   ```bash
   python -m pip install --upgrade pip 

6. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   
7. **To deactivate Environment**
   ```bash
   deactivate

### Setup on Windows

1. Follow the steps above.

2. To activate the environment:
   ```bash
   venv\Scripts\Activate

### Running the application

* The repository contains two scripts:

    **1 -** bruteforce.py : extracts the data of a single book.

    **2 -** optimized.py : extracts the data of all books in a single category.

* To run each of the scripts:
   ```bash
   python script_file.py
  
* The data is read from the files in the ```data``` folder.

### Linting

- To run Linting:
  ````bash
  flake8

## Screenshots

![Bruteforce Results](screenshots/bruteforce.png "Bruteforce Results")


![Optimized Results](screenshots/optimized.png "Optimized Results")
