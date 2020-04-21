import datetime, os

for k in os.environ:
    print(k, os.environ[k])

os.makedirs("docs", exist_ok=True)

with open("docs/index.html", "w") as f:
    f.write(f"Built at {datetime.datetime.now()}")
