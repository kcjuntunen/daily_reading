#!/bin/env python3
"""
    Get a daily reading.
    Copyright (C) 2015  K. C. Juntunen

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import json
import sys
import time
import datetime

def todays_date():
    """
    Returns today's date as a string.
    """
    now = datetime.datetime.now()
    return "{}-{}-{}".format(now.year, now.month, now.day)

def day_of_year():
    """
    Returns the day of the year as an integer.
    """
    return int(time.strftime("%j"))

if __name__ == "__main__":
    from optparse import OptionParser
    prsr = OptionParser()
    prsr.add_option("-p", "--plan"
                    , dest="json_file",
                    help="Reading plan; FILE in json format"
                    , metavar="FILE")

class DailyReading(object):
    """
    Takes a json file, and can print a daily reading passage.
    """
    def __init__(self, file_name):
        self.json_file = file_name
        try:
            with open(self.json_file, "r") as jf:
                self.schedule = json.load(jf)
        except IOError as ioe:
            sys.stderr.write("[Error {}]: Couldn't open {}\n".format(
                ioe.errno, file_name))
            return

    def get_passages(self):
        """
        Return a list containing todays passages.
        """
        if self.schedule is not None:
            return self.schedule.get("data2")[day_of_year() - 1]
        else:
            return

    def print_passages(self):
        """
        Prints a nicely formatted passage list.
        """

        info = self.schedule.get("info")
        date_string = todays_date()
        hbar_length = len(info) + len(date_string) + 4

        message = "{} -- {}\n{}\n{}\n".format(
            self.schedule.get("info"),
            date_string,
            "=" * hbar_length,
            ", ".join(self.schedule.get("data2")[day_of_year() - 1]))

        sys.stdout.writelines(message)

if __name__ == "__main__":
    from optparse import OptionParser
    prsr = OptionParser()
    prsr.add_option("-p", "--plan", dest="json_file",
                    help="Reading plan; FILE in json format", metavar="FILE")

    (options, args) = prsr.parse_args()
    pasg = DailyReading(options.json_file)
    pasg.print_passages()

