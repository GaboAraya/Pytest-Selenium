# Pytest-Selenium for UI Testing

This repository provides a framework for writing and executing UI test cases using 
the popular testing framework Pytest along with Selenium WebDriver.

---

## Features
- *Pytest Integration:* Harness the power of Pytest's flexible test discovery and execution capabilities 
to write concise and maintainable UI test cases.
- *Selenium WebDriver:* Leverage Selenium WebDriver to automate interactions with web elements, 
navigate through pages, and perform various actions required for UI testing.
- *Fixture Support:* Utilize Pytest fixtures to manage setup and teardown operations, 
enabling clean and reusable test code.
- *Parameterization:* Easily parameterize test cases to run them with different inputs 
or configurations, enhancing test coverage.
- *Reporting:* Generate detailed test reports with Allure Report, providing insights into test execution results.

---

# Getting Started

## Requirements

- Python 3.11+
- OpenJDK 11 (Optional to generate Allure-Report)

## Create a Virtual Environment: 

It's recommended to create a virtual environment to isolate project dependencies. Navigate to the project directory and create a virtual environment by running:

```
    python -m venv venv
```

Activate the virtual environment:

- On Windows:

```
    venv\Scripts\activate
```
- On macOS and Linux:

```
    source venv/bin/activate
```

## Command to install requirements

```
    pip install -r requirements.txt
```


# Run test cases

### Run all test cases by default configuration (Chrome Browser)
```
    pytest
```

### Run with different browsers (--chrome, --firefox, --edge or --cross-browser)
```
    pytest --firefox --edge
```

### Run in headless mode
```
    pytest --edge --headless
```

# Create Allure Report

It's provided a script to create the 'allure report' in the 'report' directory
```
    python .\report\create_report.py
```

