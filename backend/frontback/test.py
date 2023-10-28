import requests

response = requests.post(
    "https://labs.goo.ne.jp/api/textpair",
      json={"app_id":"eba0932dddee42c273f26d5b2cec639af9fc4ff7e0b8a86f59867b658153f798", "request_id":"record007", "text1":"高橋さんはアメリカに出張に行きました。", "text2":"山田さんはイギリスに留学している。"})
jsonData = response.json()
print(response.status_code)    # HTTPのステータスコード取得
print(jsonData["score"])    # レスポンスのHTMLを文字列で取得
