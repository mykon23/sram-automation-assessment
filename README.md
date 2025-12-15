# sram-automation-assessment
Mobile Automation Take Home Assessment

## Overview
This repository contains a mobile test automation solution created as part of the Test Automation Engineer technical assessment.

The purpose of this project is to demonstrate the ability to design and implement a maintainable automated test using Appium, while balancing correctness, readability, and scope within a limited time window.

The solution focuses on Android automation using python, pytest, and the Page Object Model.  The code is extendable to support iOS, but a single platform was prioritized for proof of concept.

## Problem Statement
The automated test performs the following actions:
1. Launch Yahoo News mobile application
1. Retrieve the text values from the bottom of the Home Screen (default screen on Android)
1. Opens a Note Taking Application (Keep notes on Android)
1. Create a new note containing the retrieved Yahoo News tab labels in a comma-separated format.


## Technology Stack
* Language: python 3
* Test Framework: pytest
* Mobile Automation: appium
* Design Pattern: Page Object Model

## Project Structure
* config/: Contains .json files necessary to start the appium session for the supported apps.  Allow for the driver to startup any app defined within the repository e.g. Yahoo News and Keep Notes.  Each platform will have its own json files and are contained within the path i.e. android is present in the path name for android applications.

* src/: Contains Page Object Model implementations for application screens.
  Pages inherit from a base page that provides common waiting and interaction logic to reduce flakiness.
  Locators are currently defined within page classes for clarity and scope control.

* tests/: Contains pytest test cases that exercise application behavior.
  Tests are written to remain environment-agnostic and rely on fixtures for driver lifecycle management.

## Design Approach

**Page Object Model**
The Yahoo News home screen is represented as a page object.
UI interactions (such as retrieving bottom navigation tab text) are encapsulated within the page, keeping test logic clean and readable.

**pytest Fixtures**

Driver setup and teardown are handled via pytest fixtures to ensure proper lifecycle management and test isolation.

**Configuration-Driven Capabilities**

Application capabilities are externalized into configuration files, allowing updates without modifying test logic.

## Running the Tests

### Prerequisites

- Android Studio and Android SDK installed
- Android emulator or real device connected
- Yahoo News and Google Keep installed on the device/emulator
- Appium Server running locally
- Update `configs/android/yahoo_news.json` so that `"appium:deviceName"` matches your emulator name

### Install Dependencies

```bash
pip3 install -r requirements.txt
```

- From the root directory.  Adjust environment variables as necessary.
```bash
PROVIDER=local PLATFORM=android PYTHONPATH=./src python3 -m pytest
```

## Future State
* Add support for running tests with iOS devices
* Move Driver creation logic away from fixture and into its respective class to construct it at runtime
* Page Objects locators to be read at runtime via config files per page
* Support Cloud Device Test Execution