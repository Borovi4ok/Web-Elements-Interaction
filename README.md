# Web Interactions Demo QA
## Table of content
+ [Introduction](#introduction)
+ [Technologies Used](#technologies-used)
+ [Installation guide](#installation-guide)
  + [Prerequisites](#prerequisites)
  + [Dependencies](#dependencies)
  + [Getting the Project](#getting-the-project)
  + [Running the Project](#running-the-project)
+ [Usage guide](#usage-guide)
  + [Tests execution](#tests-execution)
  + [Key-Driven Testing](#key-driven-testing)
  + [Generation of HTML reports](#generation-of-html-reports)
  + [Analyzing the Results](#analyzing-the-results)
  + [Modifying Test Data](#modifying-test-data)
  + [Exploring the Code](#exploring-the-code)
+ [Project description](#project-description)

Contact information

Your accomplishments and what makes this project stand out

## Introduction
Welcome to the WebInteractionDemoQA project, a unique portfolio project aimed at demonstrating a comprehensive range of skills and proficiency as an Automation Tester / Test Engineer using Python, Selenium, and Pytest. This project emphasizes hands-on experience with different web elements, mastery of Python/Selenium/Pytest methods, capability in building frameworks following different models, and the adeptness in employing various approaches to data management.

The project houses 29 test suites with a total of 133 test cases, encompassing a vast array of web elements like text boxes, checkboxes, radio buttons, tables, forms, and more. Additionally, it showcases effective interaction with dynamic properties, file transfers, modal dialogs, nested frames, tooltips, menus, and sortable/selectable/droppable/resizable elements, among others.  All the interactions are meticulously scripted using Selenium WebDriver and Python, highlighting a strong understanding of web element handling and control in automation testing.

Although every test function in this project concludes with at least one assertion, the primary focus of this portfolio project is not on implementing comprehensive testing approaches, but rather on demonstrating the abilities to handle and interact with a multitude of web elements, and build robust automation frameworks. While some forms and tables in the project may require more tests to achieve comprehensive coverage, the emphasis of this project is on the demonstration of technical skills and capabilities, rather than full test coverage.

A core part of this project is the 'data package', a testament to adept handling and structuring of complex test data. Two key files, test_data.py and excel_data.py, provide data for the classic model and Page Object Model respectively, demonstrating the use of Python for data organization, as well as using Excel data for data-driven testing.

The project utilizes a 'utility package', showcasing a sophisticated implementation of assert functions and reusable functions. The assert functions incorporate custom assertion methods for a multitude of test scenarios, such as verifying element presence, URL changes, and comparing values with tolerance, demonstrating an intermediate and above level of proficiency. The reusable functions ensure code efficiency and maintainability, with operations for data manipulation, form interaction, JavaScript execution, and more.

Lastly, this project includes 'report_logs' that provide comprehensive reports on each test suite, aiding in understanding test outcomes, spotting patterns, and improving the project's overall effectiveness.

We encourage you to delve into the project to appreciate the deftness and expertise employed in handling different web elements, managing data, and building frameworks in diverse models. By doing so, we hope you gain a better understanding of the competence and potential showcased in this portfolio project.

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

#### Tests execution:

The test suites can be executed using the Pytest command. Open a terminal/command prompt, navigate to the project directory, and run the following command:

***pytest***

You can run specific test suites by specifying the path to the suite, as in the following example:

***pytest test_package/classic_tests/test_suite_001.py***

_Replace "test_suite_001.py" with the name of the test suite you want to run._

#### Key-Driven Testing:

This project includes an example of key (or mark)-driven testing using pytest marks. Each test function within a test suite is marked with a pytest mark, allowing for tests to be easily grouped and executed together. This feature is showcased for illustrative purposes and to demonstrate the capability to implement such a testing strategy.

However, given the organization of the project, where all test functions inside a test suite (file) share an identical mark, running tests by marks or by specifying the file name in the command prompt will yield the same result. Therefore, while the pytest marks in this project technically do not provide additional functionality, they serve as a good example of how to utilize key-driven testing.

To run all tests marked with a specific key, use the '-m' option with pytest. 

For example, to run all tests marked as 'nested_frames', use:

***pytest -m nested_frames***

Similarly, to run all tests within a specific file by indicating the file name. 

For example:

***pytest test_TS_015_nested_frames.py***

_Both commands will have the same result if the mark matches all tests within the indicated file._

 #### Generation of HTML reports:

The project also supports generation of detailed HTML reports for each test suite execution. 

To create a report, use the following command:

***py.test test_package/classic_tests/test_suite_001.py --html=report.html --self-contained-html -v***
Replace "test_suite_001.py" with the name of the test suite for which to generate a report, and "report.html" with a desired name for the report file. The -v flag is for verbosity, providing detailed output in the terminal.

#### Analyzing the Results:

The results of each test suite execution are automatically recorded in the "logfile.log" file, located in either the 'tests\page_objects_model_tests' or 'tests\classic_tests' directories, depending on the tests run. This log file, created upon the first run, serves as a consolidated repository of subsequent logs unless it is renamed or relocated. It offers detailed information about each test suite, including info on passed and failed tests, as well as any errors or exceptions encountered. For a more interactive and comprehensive view of test results, an HTML report can be generated and viewed in your preferred web browser.

#### Modifying Test Data:

You can change the test data by modifying the 'test_data.py' or 'excel_data.py' files in the 'data' package, or the 'test_data_excel.xlsx' Excel spreadsheet. Please ensure that the data format is maintained to avoid errors.

#### Exploring the Code:

The project is structured to facilitate easy understanding and modification:

+ The 'data' package contains test data files, showcasing different approaches to handling test data.
+ The 'page_objects' package contains files with page objects for the tests following the Page Object Model approach. These page objects abstract the way the tests interact with the web pages.
+ The 'tests' package contains the test suites. You can explore these to understand how the tests are structured and how different web elements are interacted with.
+ The 'report_logs' package contains .log and .html reports for test suites, as well as .png screenshots captured when an error occurred.
+ The 'utilities' package contains utility scripts ('assert_functions.py' and 'reusable_functions.py'), which are used across the project to avoid code duplication and improve readability and maintainability.

## Project description
### Structure:
**WebInteractionDemoQA**
  + [data (Package)](#data-package)
    + excel_data.py
    + sampleFile.jpeg
    + test_data.py
    + test_data_excel.xlsx
  + [page_objects (Package)](#page-objects-package)
    + objects.py (Contains object files for each test suite in the Page Object Model (POM) - TS_011-TS_029)
  + [report_logs (Package)](#report-logs-package)
    + log.log (For each test suite - TS_001 - TS_029)
    + screenshots.png (Captures error scenarios)
    + log.html (Contains examples for some test suites)
  + [tests (Package)](#tests-package)
    + [classic_tests (Sub-Package)](#classic-tests-package-overview)
      + test.py (Contains test suites TS_001-TS_010)
    + [page_objects_model_tests (Sub-Package)](#page-object-model-tests-package-overview)
      + test.py (Contains test suites TS_011-TS_029)
    + [conftest.py (Setup file)](#conftest.py-file)
  + utilities (Package)
    + assert_functions.py
    + reusable_functions.py
    + 
### Inter-Page Interactions and Class Inheritance:
![image](https://github.com/Borovi4ok/Web-Elements-Interaction/assets/116018918/48c58405-ce16-4a34-b650-30ed243aeb9f)

#### Interaction Flow 1: Conftest.py, Assertions, ReusableFunctions, and Test Suites
**Technical Description**: The interaction starts with the conftest.py file, which orchestrates the setup and teardown procedures for the project. Here, a pytest fixture is utilized to initialize the WebDriver instance scoped at the class level. This WebDriver instance, commonly referred to as 'driver', is essential for managing browser interactions during the tests.

The 'driver' is shared across the project via the usefixtures decorator, which passes the instance to the Assertions and ReusableFunctions classes. Both of these utility classes have direct access to the WebDriver instance, providing reusable assertions and functions for the test suites.

The test suites, on the other hand, inherit from Assertions and ReusableFunctions classes, indirectly acquiring the WebDriver instance. Within each test suite, the WebDriver instance is passed to the PageObjects through their "***init***" method, thereby facilitating interactions with the web application.

Additionally, the conftest.py file introduces other fixtures like '***urls***' and '***action_chains***' which are centrally defined for project-wide usage. The 'urls' fixture provides a dictionary containing the URLs to be used in the tests. Each test suite, in its first test function, obtains the 'urls' instance as an argument, using the .get() method to fetch the respective URL from the dictionary for navigating to the appropriate webpage.

**Summary**: This interaction flow exemplifies efficient setup and sharing of a WebDriver instance, in addition to other important fixtures like 'urls' and 'action_chains', through the use of pytest's setup, teardown, and usefixtures facilities. It showcases code reusability and systematic session management through effective use of fixtures and class inheritance. Furthermore, it illustrates the integration of utility classes and PageObjects within the test suites, contributing to a flexible and maintainable testing framework. The design also highlights the ability to manage web navigation dynamically via the centrally managed 'urls' fixture, further enhancing the maintainability of the tests.

#### Interaction Flow 2: Test Suites and Page Object Model (POM)
**Technical Description**: In the test suites, POM classes are initialized with the WebDriver instance from the setup fixture. This allows the suite to perform actions on the web application by interacting with the web elements encapsulated in the page objects. Each test case uses these page objects to simulate user behavior.

**Summary**: This flow emphasizes the implementation of the Page Object Model, showcasing encapsulation and abstraction techniques for enhancing readability and maintainability of test cases.

#### Interaction Flow 3: Test Suites, Assertions, and ReusableFunctions
**Technical Description**: Each test suite has a test class which inherits properties from the Assertions and ReusableFunctions classes. This enables the test methods to use utility functions and assertion methods provided by these classes by simply calling 'self'. The driver from setup is passed to the test class indirectly through inheritance.

**Summary**: This interaction demonstrates effective use of class inheritance to reduce code duplication and enhance code organization.

#### Interaction Flow 4: Test Suites and TestData
**Technical Description**: In the classic model, test functions directly initiate data variables by importing the TestData class. For POM and data-driven tests, test functions fetch test data from an Excel spreadsheet via a custom get_excel_data function, which retrieves the required data based on the provided row and column names.

**Summary**: This interaction shows the ability to manage and manipulate test data using both static and dynamic methods, which are essential for a dynamic testing environment.


### Data package:
The data package serves as a cornerstone for a well-organized Python/Selenium/Pytest-based project, providing the necessary resources and data that enable efficient testing. It exemplifies effective use of Python in managing and manipulating data, including image files and Excel spreadsheets, for web interaction testing through Selenium.

This project module ensures comprehensive and efficient testing of the web interface. It also highlights the importance of effective data management and the use of data-driven testing in enhancing the overall reliability and efficiency of test automation.

#### sampleFile.jpeg: 
This image file is used in upload/download tests, testing file handling capabilities of the web interface.

#### test_data.py: 
This Python file contains the TestData class, a highly organized source of test data, for different test suites in the first part of the project (classic model). It showcases my ability to create well-structured and reusable data as well as proficiently to handle different data types such as strings, lists, and dictionaries, thereby allowing a wide range of test scenarios. These are the key methods:
+ data_text_box is used to test a text-box submit form.
+ data_add_row_table and data_edit_row_table are used to validate operations in web tables such as adding, editing, and deleting rows.
+ expected_status_respond and expected_link_url are used for link testing including API call responses and broken links.
+ download_directory and file_name are used for file transfer tests (upload/download operations).
+ expected_white and expected_red are used to verify dynamic properties like button color changes.
+ data_forms is used for form filling and submission tests.
  
This class demonstrates how various data-sets can be derived from multiple data types, including string, list, and dictionary, which are all quintessential in designing effective test cases. 

#### excel_data.py: 
This Python file features data for the second part of the project - the Page Object Model (POM) and data-driven testing. It demonstrates my proficiency in leveraging Excel data in a Selenium-based project and implementing pytest fixtures. The key methods include:
+ get_excel_row_data(test_case_name): A function that extracts data from an Excel spreadsheet based on the test_case_name. It utilizes the openpyxl library to interact with Excel documents, showing my ability to incorporate third-party libraries for specific requirements.
+ get_excel_data(): A pytest fixture which acts as a wrapper for get_excel_row_data(), enabling to fetch particular data values for test cases in a seamless manner.

#### test_data_excel.xlsx: 
This Excel spreadsheet contains the test data for the POM and data-driven tests, underscoring the ability to effectively handle and use complex data sets for test automation.

### Page objects package:
The page_objects package is a pivotal component of the project, showcasing proficiency in utilizing Python, Selenium, and Pytest to significantly streamline the testing process. The Page Object Model (POM) is utilized in the second part of this project, encompassing test suites TS_011 through TS_029. This implementation showcases a modern approach to web automation testing, enhancing test maintainability and reducing code duplication by providing a clear separation between test code and page specific code.

The package comprises multiple files/classes, with each one representing a unique page of the web application. These classes are furnished with defined methods and properties facilitating interactions with the web elements on their respective pages. This architecture helps segregate the test code from the navigation code, which in turn lends clarity and simplicity to the test scripts.

A remarkable aspect of this package is the handling of diverse locating strategies. Each class encapsulates numerous object locators – ***by ID***, ***Class***, ***linkText***, ***CSS Selector***, ***and Xpath***. This diversity ensures adaptability to varying web page structures, enabling efficient interaction with an extensive range of web elements.

Notably, the strategic use of Xpath stands out due to its ability to traverse the DOM and locate elements based on ***attributes***, ***hierarchical*** and ***relational positioning***. Proficiency in these diverse locator strategies is essential for robust web automation testing, especially when working with intricate or dynamically rendered web pages. Several locator strategies leveraging Xpath have been implemented in the project: indexing, the ***last()*** method, the ***contains()*** method, the ***text()*** method, '***and***' and '***or***' conditions, and locating ***nested child***, ***same-level*** and ***parent web-elements***.

Additional locators, based on the CSS Selector strategy, have also been implemented, including nested child, ***indexing***, and ***conditional CSS Selectors***.

Another notable feature in the page_objects package is the usage of ***chained locators***. This advanced technique enables locating elements within another, a skill invaluable when dealing with complex web pages with nested elements. This technique highlights a comprehensive understanding of the DOM structure and the ability to craft efficient, effective locator strategies.

Furthermore, the use of '***argument unpacking***' (*) when locating web elements enables passing tuples of locator strategies directly to the find methods, making the code cleaner and more efficient.

In summary, the page_objects package attests to the ability to design efficient, maintainable, and robust web automation testing solutions. Its structure facilitates reliable verification of a web application's behavior, accommodating changes in the UI without necessitating significant changes to the test scripts. This skill set is vital in a rapidly evolving web development landscape where applications are perpetually updated and refined.

### Report logs package:
The reports_logs package in this Selenium/Python automation project is a testament to the project's thorough documentation and rigorous error management approach. This package contains a collection of 29 logs (***.log***) for each test suite and case as well as error-screenshots (***.png***), and a few examples of HTML-based logs (***.html***), providing clear visibility into the testing process and results.

Each '.log' file documents the detailed step-by-step process and status of each test case (test function) for each test suite. The logs are meticulously maintained using Python's logging and inspect libraries. The logging level is set to INFO, ensuring every critical step is recorded. The assertive nature of the logs showcases the project's robust validation mechanisms and the commitment to transparency and accuracy.

Screen capture upon error is an automated feature of this project that maximizes the diagnostic capabilities. By utilizing the pytest framework's hooks and Selenium's screenshot capabilities, the system is designed to automatically capture screenshots when a test fails or an exception occurs. This visually depicts the state of the application at the point of failure, providing critical insights for troubleshooting.

Further supplementing the package are the HTML-based logs that offer an easily navigable and interactive way to explore test outcomes. Created with the help of Python's pytest-html plugin, these logs enhance the overall logging strategy, providing an alternative, user-friendly format to review test results.

In conclusion, the reports_logs package is a crucial asset to the project, offering insights into test execution, aiding in error identification, and facilitating efficient debugging. The use of advanced logging and error capturing mechanisms reaffirms the project's commitment to quality assurance, and shows my skills in implementing such sophisticated features.

### Tests package:
#### Classic tests package - overview:
The presented test suites, ranging from TS_001 to TS_010, employ a traditional approach in carrying out functional testing of a web application. They interact seamlessly with distinct components of the project and utilize a TestData file to effectively ensure reliable, maintainable, and scalable tests.

Comprising of ten comprehensive test suites, this section has been meticulously crafted to cover an extensive range of application features. Each suite validates specific functionalities:

1.	TestTextBox (TS_001): Assesses the processing of user inputs in text fields.
2.	TestCheckBoxRadio (TS_002): Evaluates the functioning of checkboxes and radio buttons.
3.	TestWebTables (TS_003): Scrutinizes interactions with web tables.
4.	TestButtons (TS_004): Checks various button actions.
5.	TestLinks (TS_005): Verifies the operation and responses of diverse links.
6.	TestBrokenLinksImages (TS_006): Certifies the handling of broken links and images.
7.	TestFileTransfer (TS_007): Confirms file upload and download functionalities.
8.	TestDynamicProperties (TS_008): Tests for a variety of dynamic properties.
9.	TestActionClick (TS_009): Verifies different click actions.
10.	TestAccordian (TS_010): Validates the functioning of Accordian elements.
    
The broad coverage of these suites underscores a strong ability to utilize Selenium WebDriver for automation testing, focusing on creating effective test strategies, managing a multitude of test cases, and ensuring comprehensive feature coverage.

Additionally, these suites serve as a testament of proficiency in Python. The code takes advantage of Python's simplicity and extensive library ecosystem to produce clear, concise, and comprehensive tests. It reflects a deeper understanding of Python's conventions and idioms and demonstrates how to effectively utilize its features in various contexts.

The suites also illustrate a familiarity with PyTest, as they skillfully incorporate its features such as fixtures, marks, and parameterization to enhance efficiency and maintainability in testing. This underlines a mastery over PyTest's capabilities, enabling the writing of scalable test codes with ease.

In summary, these test suites encapsulate a broad and deep competency in Selenium, Python, and PyTest, and showcase proficiency in software testing. Leveraging these skills, a robust and efficient testing framework was built that offers extensive coverage and high reusability, thus positioning this project as a reliable and skilled professional work sample in the field.

#### Classic tests package - detailed description:

**Test Suite 1: TestElementsPage**
The first test suite, TestElementsPage, exemplifies the ability to interact with various web elements, showcasing the skill of verifying the presence and correctness of different parts of a web page. There are five individual tests in this suite:


+ test_url_element - Confirms the successful navigation to the desired URL.
+ test_header_text - Validates the accuracy of a page's header text, ensuring correct loading and rendering of header elements.
+ test_main_menu_presence - Checks the presence of a critical component - the main menu, ensuring the page's usability.
+ test_select_message - Tests the presence and accuracy of specific page guidance messages, a key aspect of user interaction.
+ test_footer_text - Validates the presence of specific text within the page's footer.
   
The methods used in these tests demonstrate the proficient application of various locator strategies like CLASS_NAME, XPATH, and CSS_SELECTOR, which are vital for identifying web elements in Selenium WebDriver.
Furthermore, the application of pytest's marker feature (@pytest.mark.elements) illustrates the ability to categorize and filter tests for more manageable and organized test execution.

Finally, the use of custom methods from Assertions and ReusableFunctions classes reflects an understanding of code reusability and maintainability, highlighting an efficient coding approach for large-scale projects.

**Test Suite 2: TestTextBox**
The TestTextBox suite, demonstrates the ability to automate interactions with a text-box submission form, a common component across many web applications. The suite contains two main test functions:
+ test_url_box - Validates the successful navigation to the designated "text_box" URL, ensuring the page loads as expected.
+ test_submission_form - Automates the filling out of a submission form, validates the submitted data, and verifies the accuracy of the output message.
   
The test_submission_form method fills in various fields of a form, such as the name, email, current address, and permanent address fields. The fields are filled in by employing different locator strategies (CSS_SELECTOR and XPATH), demonstrating versatility in identifying and interacting with web elements.

The test also exhibits the capability to handle JavaScript commands via the Selenium WebDriver, with the use of execute_script to scroll into the view of the submit button. This highlights the proficiency in handling more complex scenarios within web automation, including interacting with JavaScript on a webpage.

Lastly, the test function verifies that the data in the output message matches the submitted data. This involves transforming a list of web elements into a list of text strings, and checking each string against the corresponding expected value. This operation reflects familiarity with list comprehension, a popular and powerful feature in Python, and also showcases the skill to perform detailed assertions based on the application's response.

**Test Suite 3: TestCheckBox**
The TestCheckBox suite reflects the capability to automate and validate interaction with checkboxes, an essential element in web forms. This suite includes seven test functions showcasing various automation strategies:

+ test_url_checkbox - Confirms the successful navigation to the specific "checkbox" URL, ensuring the correct page is loaded.
+ test_click_dropdown - Demonstrates the capability to handle dropdown elements on a webpage by expanding all dropdowns and counting the number of expanded dropdowns.
+ test_home_checkbox_message - Checks for the display of the success message upon selecting the 'Home' checkbox, validating the message displayed is as expected.
+ test_all_checkboxes_selected - Verifies that all checkboxes are selected when the parent checkbox ('Home') is selected, ensuring proper dependency functionality.
+ test_all_checkboxes_unselected - Checks that all checkboxes are deselected when the parent checkbox ('Home') is unselected, showing the ability to validate negative scenarios.
+ test_random_checkbox_selected - Tests the ability to select and deselect a random checkbox from the list, reflecting the skill to handle dynamic test data.
+ test_screenshot_checkbox - Demonstrates the capability to take a screenshot upon encountering a test failure, a crucial feature in analyzing failed test cases and reporting bugs effectively.
   
The suite incorporates various Selenium WebDriver features such as finding elements by CSS_SELECTOR and XPATH, handling exceptions, executing JavaScript commands, and manipulating web element attributes. Moreover, it demonstrates a deep understanding of Python's built-in features such as string manipulation and the random library.

Overall, this suite highlights the ability to handle complex scenarios in web automation and the proficient usage of a variety of Python and Selenium WebDriver's functionalities.

**Test Suite 4: TestRadioButtons**
The TestRadioButtons suite demonstrates my ability to automate and validate interaction with radio buttons, a crucial part of many web forms. It consists of two test functions:

+ test_url_radio_button - Confirms successful navigation to the specific "radio_button" URL, ensuring the correct page is loaded.
+ test_select_radio_buttons - Executes a more complex scenario involving multiple interactions with a set of radio buttons.
   
In the method test_select_radio_buttons, two lists of web elements are retrieved - one list containing clickable locators for radio buttons and the other comprising radio buttons with input[type='radio'] locators. These are used to perform various operations, displaying efficiency in working with multiple sets of web elements.

The test method iterates over each radio button, validates whether it is enabled, and if so, selects it. It then verifies if it is selected and if the previous button is unselected, showcasing the ability to perform detailed checks on web elements' states.

This test suite also incorporates Python's inspect module to programmatically obtain the test function's name and log it, demonstrating the understanding of Python's advanced features and the use of logging for precise test execution tracking.

Finally, if the last radio button is clicked, the test function reselects the first radio button and validates that the last radio button is unselected. This exemplifies the ability to create complex test scenarios and validate the application's behavior under varying conditions.

In summary, this test suite illustrates the capacity to interact with a variety of web elements, manipulate element attributes, perform detailed checks, and create detailed logging for test execution.

**Test Suite 5: TestWebTable**
The TestWebTable suite, shows the ability to interact with web tables - a critical element in many web applications. The suite is made up of six test functions:

+ test_url_webtable - Validates successful navigation to the "webtables" URL to ensure the correct page is loaded.
+ test_webtable_header_sorted - Verifies that the headers of the web table columns are clickable and sort the column data correctly when clicked. This test exhibits my capability to interact with table headers and validate sorting functionality.
+ test_webtable_search_field - Demonstrates my proficiency in testing the search functionality of the web table. For every column, a random value is picked and searched. I then verify that the search results contain the searched value.
+ test_webtable_add_row - I illustrate my competence in manipulating web tables by adding a new row to the table with test data and validating the addition.
+ test_webtable_edit_row - I demonstrate my ability to interact with specific table rows by locating a row with test data, editing the data in the row, and validating that the changes were successfully applied.
+ test_webtable_delete_row - This test underscores my capability to remove data from web tables by deleting a row with test data and then verifying that the row is no longer present in the table.
   
Overall, this test suite showcases the capability to interact with complex web elements like tables, manipulate the data within them, and validate their functionalities like sorting, searching, adding, editing, and deleting rows. This level of detail and comprehensive testing is crucial for web applications where data manipulation and presentation in table form are key functionalities.

**Test Suite 6: TestActionClick**
This test suite, displays the ability to interact with various types of clickable elements on a webpage by using different types of clicks.

Here are the tests included in the TestActionClick suite:

+ test_url_action - This test ensures that we've navigated to the correct page (with the "buttons" in the URL). This is important for setting up the rest of the tests.
+ test_action_double_click - In this test, I use the double_click() method from the action_chains class to double-click on a button. After performing the action, I validate that the appropriate success message is displayed.
+ test_action_right_click - utilize the context_click() method from the action_chains class to simulate a right-click on a button. After the action is executed, the verification of the correct success message is shown.
+ test_action_dynamic_click - This test demonstrates the ability to locate a button using XPath and click on it dynamically. Once the click action is performed, test confirms that the appropriate success message is shown.
  
These tests highlights proficiency in simulating different user interactions (double-click, right-click, and standard click) and validating the system's response. This suite would be crucial for testing any web application where different types of click actions lead to different outcomes.

**Test Suite 7: TestLinks**
This test suite is designed to test different types of links, specifically dynamic links and API call links, which can be vital for a web application to function correctly.

The tests included in the TestLinks suite are:

+ test_url_links - This test checks that the correct URL is accessed (with "links" in the URL), which is necessary to set the stage for the following tests.
+ test_dynamic_link - In this test, performed: click on a dynamic link, switch to the new window that it opens, and verification that the correct URL ("https://demoqa.com/") is displayed. Then, script switches back to the original window. This verifies the correct behavior of the dynamic link.
+ test_api_call_link - This test covers multiple links that send an API call when clicked. For each link, the test scrolls to the link, clicks it, and waits until the status code is updated. It verifies the status code matches the expected value. If the status code doesn't change after 5 retries (with 0.5-second waits between each), the loop breaks to prevent an infinite loop. This test verifies the API calls made by the links return the correct status codes.
   
The tests in this suite are designed to ensure that all the links on a page work correctly. Any application that heavily relies on links to perform its functionality would greatly benefit from these types of tests.

**Test Suite 8: TestBrokenLinksImages**
This test suite is designed to test both broken and functioning links and images. Web applications often include images and links, making it crucial to test whether these components are correctly displayed or direct to the right URL.

The tests included in the TestBrokenLinksImages suite are:

+ test_url_broken_links - This test checks that the correct URL is accessed (with "broken" in the URL). This sets the foundation for the tests that follow.
+ test_valid_image - This test selects an image that is supposed to be valid, verifies it's displayed, and then confirms its width, ensuring that a valid image is correctly displayed.
+ test_broken_image - Similar to the previous test, this one selects an image that is supposed to be broken, verifies it's displayed, and then checks its width. This confirms that the website handles broken images as expected.
+ test_valid_link - This test clicks on a link expected to be valid, and after a custom waiting period, it confirms that the URL of the opened page matches the expected URL. It then navigates back to the original page. This ensures valid links direct to the correct URLs.
+ test_broken_link - This test functions similarly to the previous test, but it interacts with a link that is expected to be broken. This test verifies that the website handles broken links correctly.

Overall, this test suite ensures that all images and links on a webpage behave as expected, which is crucial for a good user experience. If a website includes numerous images and links, these tests can help quickly identify any issues.

**Test Suite 9: TestFileTransfer**
This test suite is designed to verify the file upload and download functionalities of a website, which are important features for any web application that handles file transfer operations.

The tests included in the TestFileTransfer suite are:

+ test_url_file_transfer - This test is a URL verification test that ensures the appropriate webpage ("upload-download") is accessed. This serves as the foundation for the subsequent tests.
+ test_download - This test simulates a user clicking a download button on the webpage. It then checks if the download was successful by looking for the file in the default download directory within a certain time frame. This test ensures that the website's file download function works as expected.
+ test_upload - This test simulates a file upload process by sending a path of a file to the input field, without clicking the input. After the upload, it checks for the presence of a success message and verifies that the filename in the success message matches the uploaded file's name. This test verifies that the website's file upload feature is functioning correctly.
   
In conclusion, this test suite checks the crucial file transfer functionalities of a website, ensuring that users can successfully upload and download files. It also verifies the proper functioning of associated success messages and file path displays.

**Test Suite 10: TestDynamicProperties**
This test suite is designed to validate various dynamic properties that might be present on a web page. Dynamic properties can change in response to certain user actions or after a certain amount of time has passed, and validating these is crucial to ensure that the website's dynamic features function as intended.

The tests included in the TestDynamicProperties suite are:

+ test_url_dynamic_properties - This test verifies that the correct webpage ("dynamic-properties") is accessed. This test sets the foundation for the subsequent tests.
+ test_random_id - This test checks whether an element with a random ID is displayed. Random IDs can sometimes cause issues with the web application if not handled correctly, so this test verifies that the element with a random ID is rendered properly.
+ test_enable_with_delay - This test simulates a scenario where a button on the web page is expected to be enabled after a certain delay. It checks whether the button is indeed enabled after the specified delay, validating the website's time-based functionality.
+ test_button_color_change - This test checks whether the color of a button changes after a specific time period. It verifies the website's ability to dynamically update the CSS properties of an element.
+ test_visible_with_delay - This test simulates a scenario where a button becomes visible after a certain delay. It checks whether the button is indeed visible after the specified delay, validating the website's ability to dynamically show or hide elements.
   
In conclusion, this test suite helps ensure that the website's dynamic features, such as time-based functionalities and dynamic CSS updates, work as expected.

#### Page object model tests package - overview:
The second part of the project, titled "page_objects_model_tests", houses a selection of test suites that concentrate on a plethora of web elements and functionalities, all while integrating the Page Object Model (POM) design pattern. The POM design pattern integration ensures a tidy and manageable structure to the test suites, enhancing the overall readability and maintenance of the codebase.

The novelty of this part is the incorporation of Excel data-driven tests, an approach that markedly increases test flexibility and scalability. This approach allows for dynamic retrieval of test data from external sources like Excel sheets, contributing to the adaptability and scalability of the test suites. As a result, alterations in test data can be accommodated effortlessly without needing to modify the test code.

Across the entirety of the project, the prominent demonstration of proficiency in Python programming, Selenium WebDriver, JavaScript (where required), and the Pytest framework is evident. A variety of Python string manipulation techniques, list comprehensions, and date parsing/formatting operations have been utilized to cater to dynamic input and complex data scenarios.

Interaction with web elements is executed effectively through Selenium's find_elements, get_attribute, and click methods, while result verification is achieved via Pytest's assertion capabilities. Pytest's fixtures have been applied extensively, particularly for mouse hover actions and interactions with special elements.

Additionally, there are instances where JavaScript execution via Selenium's execute_script method is leveraged, enabling manipulation of elements and performing actions that might not be directly supported by Selenium WebDriver.

In terms of test design and approach, explicit waits have been incorporated for ensuring synchronization with the application under test, effectively handling dynamic elements and assuring reliable test execution. Moreover, the usage of logging facilitates the generation of informative messages, aiding in tracking test progress and results.

Overall, this part, along with the entire project, exemplifies the skill set and proficiency in Python programming, Selenium WebDriver, JavaScript (when needed), and the Pytest framework. It underscores the ability to handle various web elements, employ the POM design pattern, incorporate data-driven testing, and utilize a wide range of capabilities offered by the used technologies.

#### Page object model tests package - detailed description:
**Test Suite 11: TestForms**
+ This suite tests form input functionality using the POM design pattern.
+ It covers a variety of web elements such as input fields, radio buttons, checkboxes, dropdowns, and more.
+ Python, Selenium, and Pytest are used to automate the testing process.
+ Key features include Pytest fixtures for test environment setup, the implementation of POM for code organization, and the utilization of Selenium WebDriver for interacting with web elements.
+ The suite ensures input validation, error handling, form submission, and data persistence.

**Test Suite 12: Test Browser Windows**
+ This suite focuses on testing browser windows and tabs.
+ It interacts with URLs, success messages, and performs actions such as window switching and closing.
+ Key features include utilizing driver.close() to close extra tabs/windows, using driver.switch_to.window() to switch focus, and integration of data-driven testing with Excel sheets.
+ The suite ensures correct handling of multi-tab and multi-window scenarios.

**Test Suite 13: Test Alerts**
+ This suite automates testing of different types of alerts.
+ It deals with alert buttons, text, and result messages.
+ Key features include explicit waits for alert presence, switching focus with driver.switch_to.alert, and integration of data-driven testing with Excel sheets.
+ The suite showcases proficiency in handling alerts during automated testing.

**Test Suite 14: Test Frames**
+ This suite focuses on interacting with iframes on a web page.
+ It utilizes driver.switch_to.frame() to switch focus and validate expected text within iframes.
+ Key features include switching focus with driver.switch_to.default_content(), validation with assertion methods, and integration of data-driven testing with Excel sheets.
+ The suite demonstrates the ability to handle nested frames and ensure correct content display.

**Test Suite 15: Test Nested Frames**
+ This suite tests nested frames on a web page.
+ It handles parent and child frames and verifies content display.
+ Key features include switching focus between frames, validating expected text, and integration of data-driven testing with Excel sheets.
+ The suite demonstrates proficiency in handling nested frames and interacting with their contents.

**Test Suite 16: Test Modal Dialogs**
+ This suite automates testing of modal dialogs on a web page.
+ It interacts with dialog buttons, text, and close buttons.
+ Key features include utilizing driver.window_handles, explicit waits, and integration of data-driven testing with Excel sheets.
+ The suite ensures correct behavior and information display in modal dialogs.

**Test Suite 17: Test Accordion**
+ This suite tests an accordion component on a web page.
+ It focuses on expanding/collapsing accordion cards and verifying content visibility.
+ Key features include iterating over cards, verifying toggle indicators, custom waits, and retrieval of data from Excel sheets.
+ The suite demonstrates proficiency in handling dynamic web elements and creating custom waits.

**Test Suite 18: Test Auto Complete**
+ This suite tests auto-complete fields on a web page.
+ It interacts with color selection and verifies selected colors.
+ Key features include data retrieval and splitting, handling auto-complete options, and assertion-based verification.
+ The suite demonstrates the ability to handle dynamic input, interact with web elements, and perform data-driven testing.

**Test Suite 19: Test Date Picker**
+ This suite focuses on testing a date picker component.
+ It covers selecting a date, year, month, day, time, and verifying selected values.
+ Key features include splitting testing year, formatting dates, dynamic year creation, and parsing date and time.
+ The suite demonstrates proficiency in handling date-related scenarios and complex parsing operations.

**Test Suite 20: Test Slider**
+ This suite tests a slider component on a web page.
+ It verifies the original position of the slider thumb and sliding action.
+ Key features include retrieving slider values, performing drag-and-drop actions, and tolerance-based verification.
+ The suite demonstrates the ability to interact with and verify properties of a slider component.

**Test Suite 21: Test ProgressBar**
+ This suite tests the functionality of a progress bar on a web page.
+ It validates the initial position, progress, completion, and reset functionality of the progress bar.
+ Key features include retrieving progress information, dynamic waiting, and verifying progress bar width.
+ The suite showcases proficiency in interacting with dynamic web elements and validating progress bar behavior.

**Test Suite 22: Test Tabs**
+ This suite focuses on testing tab navigation on a web page.
+ It verifies the associated content for each tab and handles disabled tabs.
+ Key features include retrieving tabs and content, iterating through tabs, and generating informative log messages.
+ The suite demonstrates proficiency in handling tab interactions and logging informative messages.

**Test Suite 23: Test Tooltips**
+ This suite tests tooltips functionality on a web page.
+ It interacts with various elements and verifies tooltip visibility and text.
+ Key features include using actions fixture for mouse hover actions, explicit waits, and element verification.
+ The suite demonstrates proficiency in performing mouse hover actions and verifying tooltip behavior.

**Test Suite 24: Test Menu**
+ This suite tests the functionality of a menu component on a web page.
+ It interacts with main menu items, sub-items, and dropdown menus.
+ Key features include retrieving menu items, performing mouse hover actions, and verifying visibility and enabled status.
+ The suite showcases proficiency in handling menu interactions and validating menu behavior.

**Test Suite 25: Test Select Menu**
+ This suite tests select menu functionality using the POM design pattern.
+ It interacts with different types of select menus and verifies their behavior.
+ Key features include retrieving select menu elements, selecting and deleting items, and verifying selected items.
+ The suite demonstrates proficiency in handling select menus and performing data-driven testing.

**Test Suite 26: Test Sortable**
+ This suite tests sortable elements, including a list and a grid.
+ It performs drag and drop actions and verifies the resulting order.
+ Key features include retrieving sortable elements, dragging and dropping items, and verifying order.
+ The suite showcases proficiency in handling sortable elements and ensuring correct order.

**Test Suite 27: Test Selectable**
+ This suite tests selectable elements, including a list and a grid.
+ It verifies the selection status of elements based on presence/absence of selection indicators.
+ Key features include retrieving selectable elements, simulating selection, and verifying selection status.
+ The suite demonstrates proficiency in handling selectable elements and verifying selection behavior.

**Test Suite 28: Test Resizable**
+ This suite tests resizable elements, including a restricted box and an unrestricted box.
+ It interacts with the elements and validates their sizes.
+ Key features include retrieving resizable elements, obtaining size and CSS property values, and resizing using JavaScript.
+ The suite demonstrates proficiency in handling resizable elements and validating sizes.

**Test Suite 29: Test Droppable**
+ This suite tests droppable elements, covering various scenarios.
+ It performs drag and drop actions and verifies the expected behavior.
+ Key features include retrieving droppable elements, drag and drop actions, and verifying behavior.
+ The suite demonstrates versatility in handling different droppable scenarios and accurately verifying behavior.


#### conftest.py file:
The conftest.py file is an integral part of a Python-based Selenium automation testing project. It handles the configuration of the Selenium WebDriver and outlines various Pytest fixtures, which serve to set up conditions needed for running different tests.

At the start, it imports the required modules, such as Pytest, Selenium WebDriver, and its associated options, WebDriver Manager, and the project-specific test data. This operation indicates an understanding of the libraries needed for Selenium automation testing with Python and pytest.

With the **pytest_addoption** function, the code brings in flexibility in browser choice by adding a command line option. This option allows tests to run on different browsers, which is crucial for ensuring cross-browser compatibility of the application under test. The browser defaults to Chrome if none is specified.

The **setup** fixture manages the Selenium WebDriver configurations for Chrome and Firefox browsers, exemplifying knowledge in configuring and managing different browser drivers. For Chrome, it adds an option to download files to a specific directory.

The **urls** and **action_chains** fixtures are a testament to the effective implementation of the DRY (Don't Repeat Yourself) principle. These fixtures simplify tests by providing them with pre-configured data and the ActionChains object from Selenium, reducing code duplication and enhancing test maintainability.

The **pytest_runtest_makereport** function showcases advanced pytest capabilities. It uses a pytest hook to customize the test report by adding the test site URL and a screenshot when a test fails or is marked as xfail (expected to fail). This not only helps in immediate identification of test failure points but also aids in detailed debugging, ultimately improving the quality of the test suite.

In short, the **conftest.py** file is indicative of solid skills in Python, Selenium, and Pytest. It demonstrates the capability to control browser settings, reutilize test components, customize test reports, and manage various test outcomes. This file's structure and contents contribute significantly to the effectiveness and efficiency of the automation testing project.


