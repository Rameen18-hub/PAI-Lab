import requests
import re

url = "https://nishatlinen.com"  # yahan apni website ka link daalo

r = requests.get(url, timeout=10)

if r.status_code == 200:
    html = r.text

    # Title nikaalo
    title_match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if title_match:
        print("Title:", title_match.group(1).strip())

    # Saare links nikaalo
    links = re.findall(r'href="(.*?)"', html, re.IGNORECASE)
    print("\nLinks:")
    for l in links[:10]:   # pehle 10 links
        print(l)
else:
    print("Website open nahi ho rahi:", r.status_code)

