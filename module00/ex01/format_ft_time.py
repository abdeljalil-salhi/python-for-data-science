from time import time
from datetime import datetime

timestamp = time()

print(f"Seconds since January 1, 1970: {timestamp:,.4f}", end=" ")

print(f"or {timestamp:.2e} in scientific notation")

date_str = datetime.fromtimestamp(timestamp).strftime("%b %d %Y")
print(date_str)
