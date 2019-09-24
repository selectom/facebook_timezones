import unittest
import pytz
from facebook_timezones import facebookTimezoneIdToTimezoneName

class TestFacebookTimezoneIdToTimezoneName(unittest.TestCase):

    def test_is_valid_pytz_timezone(self):
        for k, v in facebookTimezoneIdToTimezoneName.iteritems():
            if k in [0, 142]:
                # These are placeholders for Unknown and the Number of Timezones
                continue
            else:
                pytz.timezone(v)

if __name__ == '__main__':
    unittest.main()