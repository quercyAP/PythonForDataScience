import time
from datetime import datetime

seconds = time.time()

formatted_seconds = "{:,.4f}".format(seconds)
scientific_notation = "{:.2e}".format(seconds)

current_date = datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {formatted_seconds} or {scientific_notation} in scientific notation")
print(current_date)
