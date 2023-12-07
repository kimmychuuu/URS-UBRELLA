import unittest
from datetime import datetime, timedelta


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



def compute_rent_fee(start: datetime, 
                    end: datetime, 
                    rate: float = 5,
                    excluded_start: str  = '',
                    excluded_end: str = ''):
    '''
    Compute rent fee from start to end based on rate.
    End should be later than start

    Parameters:
    start (datetime.datetime) : Start datetime
    end (datetime.datetime) : End datetime
    rate (float) : Rate per hour
    excluded_start (str) : Excluded start time (24h-format)
    excluded_end (str) : Excluded end time (24h-format)

    Return:
    rent (float) : Base rent
    '''
    if start > end:
        raise Exception('Invalid datetime ranges')
    
    excluded_start_time = None
    excluded_end_time = None
    if excluded_start or excluded_end:
        if not excluded_start or not excluded_end:
            raise Exception('Excluded range is required')
        
        excluded_start_time = datetime.strptime(excluded_start, '%H:%M').time()
        excluded_end_time = datetime.strptime(excluded_end, '%H:%M').time()
            
    duration = end - start
    if excluded_start_time and excluded_end_time:
        current_datetime = start
        duration = timedelta()

        while current_datetime < end:
            current_end_time = min(current_datetime + timedelta(hours=1), end)
            current_duration = current_end_time - current_datetime
            current_time = current_datetime.strftime('%H:%M')
            if not time_falls_between(current_time, excluded_start, excluded_end):
                duration += current_duration
            current_datetime += timedelta(hours=1)

    hours_rented = duration.total_seconds() / 3600
    rent = hours_rented * rate
    return rent.__floor__()


class Computation(unittest.TestCase):
    

    def setUp(self) -> None:
        return super().setUp()
    


    def test_case_exception_1(self):
        start_time = datetime(2023, 8, 3, 12, 30)
        end_time = datetime(2023, 8, 3, 6, 30)
        with self.assertRaises(Exception):
            rent = compute_rent_fee(start=start_time,
                                    end=end_time)



    def test_case_exception_2(self):
        start_time = datetime(2023, 8, 3, 12, 30)
        end_time = datetime(2023, 8, 3, 18, 30)
        excluded_start_time = '18:00'
        excluded_end_time = '06:00'
        with self.assertRaises(Exception):
            rent = compute_rent_fee(start=start_time,
                                    end=end_time,
                                    excluded_start=excluded_start_time)
            


    def test_case_exception_3(self):
        start_time = datetime(2023, 8, 3, 12, 30)
        end_time = datetime(2023, 8, 3, 18, 30)
        excluded_start_time = '18:00'
        excluded_end_time = '06:00'
        with self.assertRaises(Exception):
            rent = compute_rent_fee(start=start_time,
                                    end=end_time,
                                    excluded_end=excluded_end_time)
            


    def test_case_1(self):
        start_time = datetime(2023, 8, 3, 12, 30)
        end_time = datetime(2023, 8, 3, 18, 30)
        rent = compute_rent_fee(start=start_time,
                                end=end_time)
        self.assertEqual(rent, 30)



    def test_case_2(self):
        start_time = datetime(2023, 8, 3, 12, 30)
        end_time = datetime(2023, 8, 3, 18, 45)
        rent = compute_rent_fee(start=start_time,
                                end=end_time)
        self.assertEqual(rent, 31)


        
    def test_case_3(self):
        start_time = datetime(2023, 8, 3, 12, 30)
        end_time = datetime(2023, 8, 3, 18, 30)
        rent = compute_rent_fee(start=start_time,
                                end=end_time,
                                rate=10)
        self.assertEqual(rent, 60)



    def test_case_4(self):
        start_time = datetime(2023, 8, 3, 12, 30)
        end_time = datetime(2023, 8, 3, 18, 45)
        rent = compute_rent_fee(start=start_time,
                                end=end_time,
                                rate=10)
        self.assertEqual(rent, 62)



    def test_case_5(self):
        start_time = datetime(2023, 8, 3, 12)
        end_time = datetime(2023, 8, 4, 18)
        excluded_start_time = '20:01'
        excluded_end_time = '06:00'
        rent = compute_rent_fee(start=start_time,
                                end=end_time,
                                excluded_start=excluded_start_time,
                                excluded_end=excluded_end_time)
        self.assertEqual(rent, 100)



    def test_case_6(self):
        start_time = datetime(2023, 8, 3, 12)
        end_time = datetime(2023, 8, 5, 18)
        excluded_start_time = '20:01'
        excluded_end_time = '06:00'
        rent = compute_rent_fee(start=start_time,
                                end=end_time,
                                rate=10,
                                excluded_start=excluded_start_time,
                                excluded_end=excluded_end_time)
        self.assertEqual(rent, 340)


if __name__ == '__main__':
    unittest.main()
