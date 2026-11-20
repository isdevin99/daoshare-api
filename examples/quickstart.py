"""DaoShare API quickstart (plain HTTP, only needs `requests`).

    export DAOSHARE_TOKEN=your_api_key
    python examples/quickstart.py
"""

import os

import requests

BASE = "https://teajoin.com"
# 只有一个 API Key：优先读环境变量 DAOSHARE_TOKEN；没设置时退回占位符，
# 运行时把 "YOUR_API_KEY" 换成你的 Key 即可。不是两个 Key。
# 图省事也可以直接写：TOKEN = "你的Key"
TOKEN = os.environ.get("DAOSHARE_TOKEN", "YOUR_API_KEY")


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
