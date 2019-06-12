from aip  import AipSpeech

app_id = "14975947"
api_key="X9f3qewZCohppMHxlunznUbi"
secret_key= "LupWgIIFzZ9kTVNZSH5G0guNGZIqqTom"

client = AipSpeech(app_id,api_key,secret_key)
result = client.synthesis(
    "道友还真是狮子大开口。一条阴辰石矿脉，一年也不能精炼出一斤而已，韩道友打算一下子要走百斤，不觉得过分了点吗！", "zh", 1, {
        "vol": 5, #音量
        "spd": 4, #语速
        "pit": 8, #语调
        "per": 4, #音色 
    })

with open("audio.mp3","wb") as f:
    f.write(result)
