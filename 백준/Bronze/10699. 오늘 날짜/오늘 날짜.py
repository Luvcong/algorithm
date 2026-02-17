from datetime import datetime, timezone, timedelta

print(datetime.now(timezone(timedelta(hours=9))).strftime('%Y-%m-%d'))