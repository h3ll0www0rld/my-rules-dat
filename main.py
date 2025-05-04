import requests
import yaml

ADHOSTS_URL = "https://raw.githubusercontent.com/lingeringsound/10007/refs/heads/main/all"
REWARDHOSTS_URL = "https://raw.githubusercontent.com/lingeringsound/10007/refs/heads/main/reward"

transformed_adhosts = []
transformed_rewardhosts = []

adhosts = requests.get(ADHOSTS_URL).text
rewardhosts = requests.get(REWARDHOSTS_URL).text

for line in adhosts.split('\n'):
    if "0.0.0.0" in line:
        transformed_adhosts.append(line.replace("0.0.0.0 ",""))

for line in rewardhosts.split('\n'):
    if "0.0.0.0" in line:
        transformed_rewardhosts.append(line.replace("0.0.0.0 ",""))

with open("all.yaml", "w", encoding="utf-8") as f:
    yaml.dump({"payload":transformed_adhosts},f)

with open("reward.yaml", "w", encoding="utf-8") as f:
    yaml.dump({"payload":transformed_rewardhosts},f)
