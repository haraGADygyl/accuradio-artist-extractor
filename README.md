# accuradio-artist-extractor

## Overview
This project automates the process of extracting song artist names from www.accuradio.com - an online radio station. It checks if the artist names are already in a text file and adds them if they are not present. It utilizes Selenium, a web automation tool, to interact with the webpage, and Python for scripting.
## Files

### `project.py`
This file contains the main script for the project. Here's a breakdown of its components:

- **Constants**: Definitions of constants used throughout the script, such as the name of the artists file (`ARTISTS_FILE`), the URL of the webpage to scrape (`URL`), and the wait time between checks (`WAIT_TIME`).
- **Functions**: Several functions are defined for various tasks:
  - `extract_artist(driver)`: Extracts the song artist using Selenium.
  - `is_artist_in_file(artist)`: Checks if the artist is already in the text file.
  - `add_artist_to_file(artist)`: Adds the artist to the text file.
  - `start_chrome()`: Starts a new instance of the Chrome web browser.
  - `open_webpage(driver, url)`: Opens the webpage and agrees to terms.
  - `click_play_button(driver)`: Clicks the play button.
- **Main Function**: The `main()` function orchestrates the entire process. It starts Chrome, opens the webpage, clicks the play button, and then enters a loop where it periodically checks for the artist name, adds it to the file if it's not already present, and waits for a specified duration before repeating the process.

### `test_project.py`
This file contains test functions written using the `pytest` framework to test the functionalities of `project.py`. Here's a summary of its contents:
- **Test Functions**: Three test functions are defined to test different aspects of the main script:
  - `test_extract_artist`: Tests the `extract_artist` function.
  - `test_is_artist_in_file`: Tests the `is_artist_in_file` function.
  - `test_add_artist_to_file`: Tests the `add_artist_to_file` function.
  - `test_open_webpage`: Tests the `open_webpage` function.
  - `test_click_play_button`: Tests the `click_play_button` function.
- **Fixtures**: Two fixtures are defined to set up and clean up test environments:
  - `driver`: Starts and quits the Chrome WebDriver.

## Requirements
The `requirements.txt` file contains a list of Python packages required for the project to run. To install all dependencies from this file, you can use the following command:
```bash
pip install -r requirements.txt
```

## Usage
To use the accuradio-artist-extractor, simply run the `project.py` script. It will automatically extract artist names from the specified webpage, check if they are already in the file, and add them if necessary.

## Design Choices
- **Handling Exceptions**: Exceptions are handled explicitly, avoiding bare `except` clauses, to ensure that errors are properly caught and handled. For example, in the `extract_artist` function, a `TimeoutException` from Selenium is caught to handle timeout errors specifically.
- **File Creation**: The script checks if the artists file exists and creates it if not. This ensures that the file is present before attempting to read from it, preventing errors due to missing files.
- **Tests**: Test functions are included to verify the functionality of the main script. This ensures that changes made to the script do not break existing functionality and helps maintain code quality.

## Conclusion
The accuradio-artist-extractor project provides a convenient way to automate the extraction and management of song artist names from a web page. With clear documentation and comprehensive test coverage, it ensures reliability and maintainability.