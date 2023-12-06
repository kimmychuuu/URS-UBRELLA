from datetime import datetime, timedelta

class machineutils:

    @staticmethod
    def time_falls_between(time, start, end, hour_interval=1):
        checked_datetime = datetime.strptime(time, "%H:%M")
        start_datetime = datetime.strptime(start, "%H:%M")
        end_datetime = datetime.strptime(end, "%H:%M")

        if start_datetime > end_datetime:
            end_datetime += timedelta(days=1)
            if checked_datetime >= datetime(1900, 1, 1) \
                and checked_datetime <= end_datetime - timedelta(days=1):
                checked_datetime += timedelta(days=1)

        if checked_datetime >= start_datetime and checked_datetime <= end_datetime:
            return True

        return False
