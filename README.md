[![Downloads](https://pepy.tech/badge/apptracker)](https://pepy.tech/project/apptracker)
[![HitCount](http://hits.dwyl.io/manojpawarsj12/Pyapplicationtracker.svg)](http://hits.dwyl.io/manojpawarsj12/Pyapplicationtracker)  [![PyPI version](https://badge.fury.io/py/apptracker.svg)](https://badge.fury.io/py/apptracker)  [![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
AppTracker is a Python application designed to track and visualize application usage over time. It records the active applications and their usage duration, allowing users to analyze their activity patterns through interactive visualizations.

## Features

- **Activity Tracking**: Automatically records the active window and its usage time.
- **Data Storage**: Stores usage data in a structured JSON format for easy access and manipulation.
- **Visualizations**: Generates interactive pie charts using Plotly to visualize application usage.
- **Time Range Selection**: Allows users to view usage data for specific time ranges, including daily, weekly, monthly, or custom date selections.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd apptracker
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To start tracking your application usage, run the following command:
```
python apptracker/main.py -start
```

To view your application usage in a pie chart, use:
```
python apptracker/main.py -show
```

To clear your recorded usage data, execute:
```
python apptracker/main.py -clean
```

## Configuration

Configuration settings can be adjusted in `apptracker/config/settings.py`. This includes default time ranges for visualizations and other application-specific settings.

## License

This project is licensed under the MIT License. See the LICENSE file for details.