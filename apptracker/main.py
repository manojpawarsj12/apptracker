from argparse import ArgumentParser
from apptracker.utils.activity_manager import ActivityManager
from apptracker.utils.data_handler import read_activities
from apptracker.visualizations.plot_generator import PlotGenerator
from datetime import datetime
import platform


def main():
    parser = ArgumentParser(description="AppTracker: A cross-platform application tracker")
    parser.add_argument('-start', action='store_true', help='Start tracking your application usage')
    parser.add_argument('-show', action='store_true', help='Display usage statistics in a pie chart')
    parser.add_argument('-clean', action='store_true', help='Clear all tracked data')
    parser.add_argument('-range', type=str, default='today', help='Specify time range: today, week, month, or custom date')
    parser.add_argument('-platform', action='store_true', help='Show the current platform information')

    args = parser.parse_args()
    activity_manager = ActivityManager()

    if args.clean:
        activity_manager.clear_activities()
    elif args.start:
        activity_manager.record_activities()
    elif args.show:
        time_range = args.range
        activities = read_activities()
        plot_generator = PlotGenerator(activities)
        plot_generator.show_activity(time_range)
    elif args.platform:
        print(f"Running on platform: {platform.system()} ({platform.release()})")
    else:
        print("No valid command provided. Use -start, -show, -clean, or -platform.")

if __name__ == "__main__":
    main()