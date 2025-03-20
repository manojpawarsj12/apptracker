from datetime import datetime
import time
from apptracker.utils.time_utils import parse_time_entry, format_time_for_display
from apptracker.utils.data_handler import read_activities, write_activities
from apptracker.utils.tracker import get_active_window_name
class ActivityManager:
    def __init__(self):
        self.activities = []

    def initialize_activities(self):
        data = read_activities()
        self.activities = self.get_activities_from_json(data)

    def get_activities_from_json(self, data):
        return [
            Activity(
                name=activity['name'],
                time_entries=self.get_time_entries_from_json(activity)
            ) for activity in data.get('activities', [])
        ]

    def get_time_entries_from_json(self, activity):
        return [
            TimeEntry(
                start_time=parse_time_entry(entry['start_time']),
                end_time=parse_time_entry(entry['end_time']),
                days=entry['days'],
                hours=entry['hours'],
                minutes=entry['minutes'],
                seconds=entry['seconds']
            ) for entry in activity.get('time_entries', [])
        ]

    def record_time_entry(self, activity_name, start_time, end_time):
        time_entry = TimeEntry(start_time, end_time)
        for activity in self.activities:
            if activity.name == activity_name:
                activity.time_entries.append(time_entry)
                break
        else:
            self.activities.append(Activity(activity_name, [time_entry]))

        write_activities(self.serialize())

    def serialize(self):
        return {
            'activities': [activity.serialize() for activity in self.activities]
        }

    def record_activities(self):
        print("Recording activities. Press CTRL+C to stop.")
        try:
            self.initialize_activities()
        except Exception:
            print("No existing activity data found. Starting fresh.")

        active_window_name = None
        start_time = datetime.now()

        try:
            while True:
                new_window_name = get_active_window_name()
                if new_window_name != active_window_name:
                    if active_window_name:
                        end_time = datetime.now()
                        self.record_time_entry(active_window_name, start_time, end_time)
                        start_time = datetime.now()
                    active_window_name = new_window_name
                time.sleep(1)
        except KeyboardInterrupt:
            if active_window_name:
                end_time = datetime.now()
                self.record_time_entry(active_window_name, start_time, end_time)
            print("Activity recording stopped.")

    def clear_activities(self):
        """Clear all recorded activities and save the empty state."""
        confirmation = input("Are you sure you want to clear all activity data? (y/n): ")
        if confirmation.lower() == 'y':
            self.activities = []
            write_activities(self.serialize())
            print("All activity data has been cleared.")
        else:
            print("Operation cancelled.")


class Activity:
    def __init__(self, name, time_entries):
        self.name = name
        self.time_entries = time_entries

    def serialize(self):
        return {
            'name': self.name,
            'time_entries': [entry.serialize() for entry in self.time_entries]
        }


class TimeEntry:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.total_time = end_time - start_time
        self.days, self.hours, self.minutes, self.seconds = self._calculate_time_components()

    def _calculate_time_components(self):
        days = self.total_time.days
        seconds = self.total_time.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return days, hours, minutes, seconds

    def serialize(self):
        return {
            'start_time': format_time_for_display(self.start_time),
            'end_time': format_time_for_display(self.end_time),
            'days': self.days,
            'hours': self.hours,
            'minutes': self.minutes,
            'seconds': self.seconds
        }