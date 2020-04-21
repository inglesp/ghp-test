import datetime, os

os.makedirs("output", exist_ok=True)

with open("output/index.html", "w") as f:
    f.write(f"Built at {datetime.datetime.now()}")
