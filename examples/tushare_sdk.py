"""Use the official Tushare SDK against DaoShare.

    pip install tushare
    python examples/tushare_sdk.py
"""

import tushare as ts

# 把下面的占位符换成你兑换到的 API Key（只有一个 Key）
TOKEN = "YOUR_API_KEY"

# 下面两处用的是同一个 TOKEN 变量，不是两个 Key：
# SDK 要求先设全局 token，再同步到 pro_api() 创建的实例上。
ts.set_token(TOKEN)
pro = ts.pro_api()
pro._DataApi_token = TOKEN
pro._DataApi__http_url = "https://teajoin.com"

df = pro.daily(ts_code="000001.SZ", start_date="20260101", end_date="20260131")
print(df.head())
print(f"{len(df)} rows")
