import datetime, os

os.makedirs("docs", exist_ok=True)

with open("docs/index.html", "w") as f:
    f.write(f"Built at {datetime.datetime.now()}")
