"""DaoShare API quickstart (plain HTTP, only needs `requests`).

    python examples/quickstart.py
"""

import requests

BASE = "https://teajoin.com"
# 把下面的占位符换成你兑换到的 API Key（只有一个 Key）
TOKEN = "YOUR_API_KEY"


def query(api_name, **params):
    """Call one endpoint and return its data block."""
    resp = requests.post(
        BASE,
        json={"api_name": api_name, "token": TOKEN, "params": params},
        timeout=30,
    )
    resp.raise_for_status()
    body = resp.json()
    if body.get("code") != 0:
        raise RuntimeError(body.get("msg") or body)
    return body["data"]


if __name__ == "__main__":
    data = query(
        "daily",
        ts_code="000001.SZ",
        start_date="20260101",
        end_date="20260131",
    )
    print("fields:", data["fields"])
    for row in data["items"][:5]:
        print(row)
    print(f"{len(data['items'])} rows, has_more={data['has_more']}")
