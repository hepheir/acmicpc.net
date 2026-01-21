# 1340번: 연도 진행바

from datetime import datetime


c_date = datetime.strptime(input(), '%B %d, %Y %H:%M')

s_date = datetime(c_date.year, 1, 1)
e_date = datetime(c_date.year+1, 1, 1)

print((c_date-s_date) / (e_date-s_date) * 100)
