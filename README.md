# Web Interactions Demo QA
## Table of content
[Introduction](#Introduction)

Information about the technologies used

Installation guide

Usage guide

Tests descriptions

Contact information

Your accomplishments and what makes this project stand out

## Introduction
Welcome to the WebInteractionDemoQA repository, a testament to the extensive proficiency and skills in Python, Selenium, and Pytest that have been utilized to build a robust and comprehensive test automation project. Comprising a total of 29 test suites and 133 test cases, the project is divided into two sections that exemplify two distinct testing approaches - the classic model and the page object model.

The project stands out for its interaction with a wide array of web elements, such as text boxes, checkboxes, radio buttons, tables, file transfers, dynamic properties, forms, modal dialogs, and more. All the interactions are meticulously scripted using Selenium WebDriver and Python, highlighting a strong understanding of web element handling and control in automation testing.

A core part of this project is the 'data package', a testament to adept handling and structuring of complex test data. Two key files, test_data.py and excel_data.py, provide data for the classic model and Page Object Model respectively, demonstrating the use of Python for data organization, as well as using Excel data for data-driven testing.

The project utilizes a 'utility package', showcasing a sophisticated implementation of assert functions and reusable functions. The assert functions incorporate custom assertion methods for a multitude of test scenarios, such as verifying element presence, URL changes, and comparing values with tolerance, demonstrating an intermediate and above level of proficiency. The reusable functions ensure code efficiency and maintainability, with operations for data manipulation, form interaction, JavaScript execution, and more.

The test suites showcase the use of both classic and page object model testing approaches, each contributing uniquely to the project's success. conftest.py, a pivotal file, serves to share the WebDriver instance across the project, facilitating interactions with the web application.

Lastly, this project includes 'report_logs' that provide comprehensive reports on each test suite, aiding in understanding test outcomes, spotting patterns, and improving the project's overall effectiveness.

This portfolio is a testament to strong abilities in writing efficient, reusable, and maintainable test automation scripts using Python, Selenium, and Pytest. It demonstrates a profound understanding of automation testing principles, hands-on experience with Selenium WebDriver, and a knack for crafting organized and scalable test data. The implemented solutions are a blend of complexity, necessity, and innovation, aimed at providing a positive impact on the projects they are employed in.

## Installation Guide

To run this test automation project on your local machine, you need to follow these steps:

### Prerequisites:

Ensure you have the following software installed on your machine:

+ Python 3.x: Download and install from python.org.

  _Pip: Python's package installer should be installed automatically with Python. You can check whether it's installed by running **_pip --version_** in your terminal/command prompt._

+ Git: Download and install from git-scm.com.

+ A Python IDE or code editor, such as PyCharm or Visual Studio Code.

  + PyCharm: Download and install from jetbrains.com/pycharm

  + Visual Studio Code: Download and install from code.visualstudio.com

### Dependencies:

This project has a few dependencies which can be installed via pip:

+ Selenium

+ Pytest

+ Openpyxl

To install these, run the following command in your terminal/command prompt:

***pip install selenium pytest openpyxl***


**Getting the Project:**

Open a terminal/command prompt, navigate to the directory where you want to clone this project.

Clone the repository by running the following command:

***git clone https://github.com/YourGitHubUsername/WebInteractionDemoQA.git***

_Replace "YourGitHubUsername" with your actual GitHub username._


**Running the Project:**

Once the project is cloned, navigate to the project directory (WebInteractionDemoQA) in your terminal/command prompt and run the pytest command to start the tests:

***pytest***

_Note: Make sure that you're in the correct directory before running the pytest command. The terminal should look something like this:_

***C:\Users\YourUsername\directory\WebInteractionDemoQA>pytest***

_Replace "YourUsername" and "directory" with your actual username and the directory where you cloned the project._

Congratulations! The test suites should now start executing. The results will be logged in the 'report_logs' directory, and you can review them at your convenience.

For any issues encountered during the installation or running of the project, please open a new issue in the GitHub repository.
