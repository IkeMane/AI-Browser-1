

# Project Setup Instructions

This guide outlines the steps needed to set up and run the provided Python script on a macOS environment. The script uses `pynput` to handle keyboard shortcuts and a custom module named `Browsing` to perform web interactions.

## Prerequisites

Before proceeding with the setup, make sure you have Python installed on your machine. You can download and install Python from [python.org](https://www.python.org/downloads/).

## Installation

1. **Clone the Repository:**
   Begin by cloning the repository to your local machine, or download the ZIP file and extract it.

2. **Install Required Packages:**
   Install the required Python libraries listed in the `requirements.txt` file. You can do this using the following command:

   ```bash
   pip install -r requirements.txt
   ```

3. **Grant Accessibility Permissions:**
   The `pynput` library needs accessibility permissions to control the keyboard on macOS:

   - Open `System Preferences`.
   - Navigate to `Security & Privacy`.
   - Go to the `Privacy` tab.
   - Select `Accessibility` from the list on the left.
   - Click the lock icon at the bottom left to make changes (you may need to enter your password).
   - Click the `+` button and add your Python executable (you can find your Python path by running `which python3` in the terminal).
   - Also add your Terminal application to grant it permissions.


## Usage

Once the script is running, it will listen for the specific hotkey combination (`Command+Shift+F`). When this hotkey is activated, it will perform the programmed actions, such as analyzing content on a webpage and interacting with it.

### Note:
- Ensure your web browser is open and accessible as the script attempts to interact with it.
- You may need to adjust the script depending on your web browser and its settings.

## Troubleshooting

If you encounter issues with the script, make sure all permissions are correctly set, and the required modules are installed. Check the Python console output for any error messages that can help in diagnosing the problem.
