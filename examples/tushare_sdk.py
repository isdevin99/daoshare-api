"""Use the official Tushare SDK against DaoShare.

    pip install tushare
    export DAOSHARE_TOKEN=your_api_key
    python examples/tushare_sdk.py
"""

import os

import tushare as ts

TOKEN = os.environ.get("DAOSHARE_TOKEN", "YOUR_API_KEY")

# 下面两处写的是同一个 Key，不是两个：
# set_token 设全局 token，pro_api() 建实例后再同步到实例上。
ts.set_token(TOKEN)
pro = ts.pro_api()
pro._DataApi_token = TOKEN
pro._DataApi__http_url = "https://teajoin.com"

df = pro.daily(ts_code="000001.SZ", start_date="20260101", end_date="20260131")
print(df.head())
print(f"{len(df)} rows")
