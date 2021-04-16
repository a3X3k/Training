exec("""\ndef check_leap_year(leap_year):\n    return((leap_year%4==0 and leap_year%100!=0) or leap_year%400==0)\n\nleap_year=input()\nprint(check_leap_year(int(leap_year)))\n""")
