# Web Interactions Demo QA
## Table of content
[Introduction](#Introduction)

Technologies Used

Installation guide

Usage guide

Tests descriptions

Contact information

Your accomplishments and what makes this project stand out

## Introduction
Welcome to the WebInteractionDemoQA repository, a testament to the extensive proficiency and skills in Python, Selenium, and Pytest that have been utilized to build a robust and comprehensive test automation project. Comprising a total of 29 test suites and 133 test cases, the project is divided into two sections that exemplify two distinct testing approaches - the classic model and the page object model.

The project stands out for its interaction with a wide array of web elements, such as text boxes, checkboxes, radio buttons, tables, file transfers, dynamic properties, forms, modal dialogs, links, images, browser windows, alerts, frames, auto complete, date picker, slider, progress bars, tooltips, sortable, selectable, droppable, resizable elements, and more. All the interactions are meticulously scripted using Selenium WebDriver and Python, highlighting a strong understanding of web element handling and control in automation testing.

A core part of this project is the 'data package', a testament to adept handling and structuring of complex test data. Two key files, test_data.py and excel_data.py, provide data for the classic model and Page Object Model respectively, demonstrating the use of Python for data organization, as well as using Excel data for data-driven testing.

The project utilizes a 'utility package', showcasing a sophisticated implementation of assert functions and reusable functions. The assert functions incorporate custom assertion methods for a multitude of test scenarios, such as verifying element presence, URL changes, and comparing values with tolerance, demonstrating an intermediate and above level of proficiency. The reusable functions ensure code efficiency and maintainability, with operations for data manipulation, form interaction, JavaScript execution, and more.

The test suites showcase the use of both classic and page object model testing approaches, each contributing uniquely to the project's success. conftest.py, a pivotal file, serves to share the WebDriver instance across the project, facilitating interactions with the web application.

Lastly, this project includes 'report_logs' that provide comprehensive reports on each test suite, aiding in understanding test outcomes, spotting patterns, and improving the project's overall effectiveness.

This portfolio is a testament to strong abilities in writing efficient, reusable, and maintainable test automation scripts using Python, Selenium, and Pytest. It demonstrates a profound understanding of automation testing principles, hands-on experience with Selenium WebDriver, and a knack for crafting organized and scalable test data. The implemented solutions are a blend of complexity, necessity, and innovation, aimed at providing a positive impact on the projects they are employed in.


## Technologies Used
This project utilizes a combination of modern technologies and methodologies in the field of automation testing. Here's an overview of the primary tools and frameworks used:

**Pytho**n: The backbone of the project, Python is a powerful, flexible programming language that's widely used in automation testing for its clear, readable syntax and vast library support.

**Selenium**: An open-source web testing framework, Selenium enables the automation of browser activities. It's used in this project for automating interactions with various web elements and forms, enhancing the efficiency and reliability of the tests.

**Pytest**: A robust testing framework for Python, Pytest makes it simple to write small tests, yet scales to support complex functional testing. This project leverages Pytest for structuring and executing tests, providing readable reports, and allowing the integration of numerous plugins for additional functionalities.

**Openpyxl**: This Python library is used to read and write Excel 2010 xlsx/xlsm/xltx/xltm files. It's employed in this project for handling test data stored in Excel spreadsheets, enabling data-driven testing.

**Page Object Model (POM)**: A design pattern that improves test maintenance and reduces code duplication. The project incorporates the POM approach for many of its tests, enhancing the readability and scalability of the test suites.

**GitHub**: All project code is hosted on GitHub, a platform that supports version control and collaboration. It's a demonstration of good coding practices and modern software development workflows.

**IDE (PyCharm or Visual Studio Code)**: The development of this project was conducted in a professional IDE environment (like PyCharm or VS Code), leveraging features such as intelligent code completion, linting, and integrated terminal for efficient code writing and debugging.

## Installation Guide
To run this test automation project on your local machine, you need to follow these steps:

#### Prerequisites:

Ensure you have the following software installed on your machine:

+ Python 3.x: Download and install from python.org.

  _Pip: Python's package installer should be installed automatically with Python. You can check whether it's installed by running **_pip --version_** in your terminal/command prompt._

+ Git: Download and install from git-scm.com.

+ A Python IDE or code editor, such as PyCharm or Visual Studio Code.

  + PyCharm: Download and install from jetbrains.com/pycharm

  + Visual Studio Code: Download and install from code.visualstudio.com

#### Dependencies:

This project has a few dependencies which can be installed via pip:

+ Selenium

+ Pytest

+ Openpyxl

To install these, run the following command in your terminal/command prompt:

***pip install selenium pytest openpyxl***


#### Getting the Project:

Open a terminal/command prompt, navigate to the directory where you want to clone this project.

Clone the repository by running the following command:

***git clone https://github.com/YourGitHubUsername/WebInteractionDemoQA.git***

_Replace "YourGitHubUsername" with your actual GitHub username._


#### Running the Project:

Once the project is cloned, navigate to the project directory (WebInteractionDemoQA) in your terminal/command prompt and run the pytest command to start the tests:

***pytest***

_Note: Make sure that you're in the correct directory before running the pytest command. The terminal should look something like this:_

***C:\Users\YourUsername\directory\WebInteractionDemoQA>pytest***

_Replace "YourUsername" and "directory" with your actual username and the directory where you cloned the project._

Congratulations! The test suites should now start executing. The results will be logged in the 'report_logs' directory, and you can review them at your convenience.

For any issues encountered during the installation or running of the project, please open a new issue in the GitHub repository.

## Usage Guide
Once you've followed the installation instructions and successfully set up the project on your local machine, you're ready to run the tests and explore the project. Here's a guide to help you get started:

Running the Tests:

The test suites can be executed using the Pytest command. Open a terminal/command prompt, navigate to the project directory, and run the following command:

bash
Copy code
pytest
You can run specific test suites by specifying the path to the suite, as in the following example:

bash
Copy code
pytest test_package/classic_tests/test_suite_001.py
Replace "test_suite_001.py" with the name of the test suite you want to run.

Key-Driven Testing:

This project uses key (or mark)-driven testing. Each test function within a test suite is marked with a pytest mark. This allows for tests to be easily grouped and executed together. To run all tests marked with a specific key, use the '-m' option with pytest. For example, to run all tests marked as 'nested_frames', use:

bash
Copy code
pytest -m nested_frames
Generating HTML Reports:

The project also supports generation of detailed HTML reports for each test suite execution. To create a report, use the following command:

bash
Copy code
py.test test_package/classic_tests/test_suite_001.py --html=report.html --self-contained-html -v
Replace "test_suite_001.py" with the name of the test suite for which you want to generate a report, and "report.html" with your desired name for the report file. The -v flag is for verbosity, providing detailed output in the terminal.

Analyzing the Results:

The results of each test suite execution are stored in the 'report_logs' directory. You'll find detailed logs for each test suite, including information about passed and failed tests, and any errors or exceptions that occurred. Additionally, you can open the HTML report in your web browser for a more interactive and comprehensive view of the test results.

Modifying Test Data:

You can change the test data by modifying the 'test_data.py' or 'excel_data.py' files in the 'data' package, or the 'test_data_excel.xlsx' Excel spreadsheet. Please ensure that the data format is maintained to avoid errors.

Exploring the Code:

The project is structured to facilitate easy understanding and modification:

The 'test' package contains the test suites. You can explore these to understand how the tests are structured and how different web elements are interacted with.
The 'page_objects' package contains files with page objects for the tests following the Page Object Model approach. These page objects abstract the way the tests interact with the web pages.
The 'data' package contains test data files, showcasing different approaches to handling test data.
The 'utility' package contains utility scripts ('assert_functions.py' and 'reusable_functions.py'), which are used across the project to avoid code duplication and improve readability and maintainability.
Feel free to explore the code, run the tests, modify the test data, and even improve the test suites. If you encounter any issues or have any questions, please open a new issue in the GitHub repository. Enjoy testing!
