# File: /apptracker/apptracker/apptracker/config/settings.py

DEFAULT_TIME_RANGE = {
    "today": {
        "start": "2023-10-01T00:00:00",
        "end": "2023-10-01T23:59:59"
    },
    "week": {
        "start": "2023-09-25T00:00:00",
        "end": "2023-10-01T23:59:59"
    },
    "month": {
        "start": "2023-09-01T00:00:00",
        "end": "2023-10-01T23:59:59"
    },
    "custom": {
        "start": None,
        "end": None
    }
}

PLOTLY_SETTINGS = {
    "theme": "plotly",
    "showlegend": True,
    "hoverinfo": "label+percent",
    "textinfo": "value+percent",
    "marker": {
        "line": {
            "color": "#000000",
            "width": 2
        }
    }
}

JSON_FILE_PATH = "data/activities.json"