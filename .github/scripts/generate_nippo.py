import os
from openai import OpenAI
from datetime import date

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

today = date.today().isoformat()

prompt = f"""
今日は{today}です。
私が行ったエンジニア学習を、時系列で箇条書きでMarkdown形式で出力してください。
何も学習していなければ「今日はエンジニア学習をしていませんでした。」とだけ出力してください。
出力は以下の形式に従ってください：

# {today} の学習記録
– 学習内容1
– 学習内容2
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.4,
)

content = response.choices[0].message.content.strip()

# 学習していなければスキップ
if "今日はエンジニア学習をしていませんでした。" in content:
    print("🛑 学習記録がないためスキップします。")
    exit(0)

# 追記
with open("nippo.md", "a") as f:
    f.write("\n" + content + "\n\n")

print("✅ nippo.md に追記しました")
