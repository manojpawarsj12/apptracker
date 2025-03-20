from datetime import datetime, timedelta
import plotext as plt
import math


class PlotGenerator:
    def __init__(self, activities):
        self.activities = activities

    def generate_pie_chart(self, title="Your Usage Activity"):
        labels = [activity["name"] for activity in self.activities]
        values = [self.calculate_total_time(activity) for activity in self.activities]

        values_minutes = [v / 60 for v in values]

        total = sum(values_minutes)
        percentages = [
            round((v / total) * 100, 1) if total > 0 else 0 for v in values_minutes
        ]

        display_labels = [
            f"{label} ({pct}%)" for label, pct in zip(labels, percentages)
        ]

        plt.clear_figure()
        plt.theme("dark")

        sorted_data = sorted(
            zip(display_labels, values_minutes), key=lambda x: x[1], reverse=True
        )
        sorted_labels, sorted_values = zip(*sorted_data) if sorted_data else ([], [])

        plt.bar(sorted_labels, sorted_values)
        plt.title(title)
        plt.xlabel("Applications")
        plt.ylabel("Usage Time (minutes)")
        plt.show()

        # Print additional information as text
        print("\n" + "=" * 50)
        print(f"\n{title} (Pie Chart View)")
        print("=" * 50)

        sorted_data = sorted(
            zip(labels, values, percentages), key=lambda x: x[1], reverse=True
        )

        print("\nDetailed Usage:")
        for label, value, percentage in sorted_data:
            hours = math.floor(value / 3600)
            minutes = math.floor((value % 3600) / 60)
            seconds = value % 60
            time_str = f"{hours}h {minutes}m {seconds}s"
            print(f"  {label}: {time_str} ({percentage}%)")

    def calculate_total_time(self, activity):
        total_seconds = 0
        for entry in activity["time_entries"]:
            total_seconds += (
                (entry["days"] * 86400)
                + (entry["hours"] * 3600)
                + (entry["minutes"] * 60)
                + entry["seconds"]
            )
        return total_seconds

    def generate_time_range_visualization(self, start_date, end_date):
        filtered_activities = self.filter_activities_by_date(start_date, end_date)
        self.generate_pie_chart(title=f"Usage Activity from {start_date} to {end_date}")

    def filter_activities_by_date(self, start_date, end_date):
        filtered = []
        for activity in self.activities.get("activities", []):
            filtered_entries = []
            for entry in activity.get("time_entries", []):
                # Convert the string times into datetime objects before filtering
                entry_start = datetime.strptime(
                    entry.get("start_time", ""), "%Y-%m-%d %H:%M:%S"
                )
                entry_end = datetime.strptime(
                    entry.get("end_time", ""), "%Y-%m-%d %H:%M:%S"
                )

                if start_date <= entry_start <= end_date:
                    filtered_entries.append(entry)

            if filtered_entries:
                filtered.append(
                    {"name": activity["name"], "time_entries": filtered_entries}
                )
        return filtered

    def show_activity(self, time_range):
        if time_range == "today":
            start_date = datetime.now().replace(
                hour=0, minute=0, second=0, microsecond=0
            )
            end_date = datetime.now()
        elif time_range == "week":
            start_date = datetime.now() - timedelta(days=7)
            end_date = datetime.now()
        elif time_range == "month":
            start_date = datetime.now() - timedelta(days=30)
            end_date = datetime.now()
        else:
            try:
                start_date, end_date = map(
                    lambda x: datetime.strptime(x.strip(), "%Y-%m-%d"),
                    time_range.split(","),
                )
            except ValueError:
                print("Invalid date range format. Use 'YYYY-MM-DD,YYYY-MM-DD'.")
                return

        filtered_activities = self.filter_activities_by_date(start_date, end_date)
        if filtered_activities:
            self.activities = filtered_activities
            self.generate_pie_chart(
                title=f"Usage Activity from {start_date.date()} to {end_date.date()}"
            )
        else:
            print("No activities found for the specified time range.")

    def generate_bar_chart(self, title="Your Usage Activity"):
        """Add a bar chart visualization option"""
        labels = [activity["name"] for activity in self.activities]
        values = [
            self.calculate_total_time(activity) / 60 for activity in self.activities
        ]  # Convert to minutes

        # Sort by value for better visualization
        sorted_data = sorted(zip(labels, values), key=lambda x: x[1], reverse=True)
        sorted_labels, sorted_values = zip(*sorted_data) if sorted_data else ([], [])

        plt.clear_figure()
        plt.theme("dark")
        plt.bar(sorted_labels, sorted_values)
        plt.title(title)
        plt.xlabel("Applications")
        plt.ylabel("Usage Time (minutes)")
        plt.show()
