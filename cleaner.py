#!/usr/bin/python

import sys
import re
import time

for line in sys.stdin:
  oline = line.strip()
  line = re.sub("[^\s\.0-9a-zA-Z]",'',line,re.IGNORECASE)
  m = re.match("([0-9]{2}\s[a-z]{3}\s[0-9]{2})\s*([\w\s\.\/]*)\s{4,}(\d{1,}\.\d\d)(\s-)*", line,re.IGNORECASE)
  if m:
      date = time.strptime(m.group(1).strip(),'%d %b %y')
      strdate = time.strftime("%d-%m-%Y",date)
      trans = m.group(2).strip()
      amount = m.group(3).strip()
      if oline.endswith('-'):
        amount = "0,%s" % (amount)


      print '"%s","%s",%s' % (strdate, trans, amount)
