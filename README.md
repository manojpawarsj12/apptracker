[![Downloads](https://pepy.tech/badge/apptracker)](https://pepy.tech/project/apptracker)
[![HitCount](http://hits.dwyl.io/manojpawarsj12/Pyapplicationtracker.svg)](http://hits.dwyl.io/manojpawarsj12/Pyapplicationtracker)
[![PyPI version](https://badge.fury.io/py/apptracker.svg)](https://badge.fury.io/py/apptracker)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

# AppTracker

AppTracker is a Python application designed to track and visualize application usage over time. It records the active applications and their usage duration, allowing users to analyze their activity patterns through interactive visualizations.

## Features

- **Activity Tracking**: Automatically records the active window and its usage time.
- **Data Storage**: Stores usage data in a structured JSON format for easy access and manipulation.
- **Visualizations**: Generates interactive pie charts using Plotly to visualize application usage.
- **Time Range Selection**: Allows users to view usage data for specific time ranges, including daily, weekly, monthly, or custom date selections.

## Installation

### Cloning the Repository

1. Clone the repository:
   ```bash
   git clone https://github.com/manojpawarsj12/apptracker
   cd apptracker
   ```

### Creating a Virtual Environment

2. Create and activate a virtual environment:
   - On macOS/Linux:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

### Installing Dependencies

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Use the following commands to operate AppTracker:

- **Start Tracking**:
  Begin tracking your application usage.
  ```bash
  python -m apptracker.main -start
  ```

- **Show Visualizations**:
  View your application usage in a pie chart.
  ```bash
  python -m apptracker.main -show
  ```

- **Clear Recorded Data**:
  Clear your recorded usage data.
  ```bash
  python -m apptracker.main -clean
  ```

## Configuration

You can adjust configuration settings in `apptracker/config/settings.py`. This includes default time ranges for visualizations and other application-specific settings.



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
