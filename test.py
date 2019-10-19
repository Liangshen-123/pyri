from aip import AipSpeech
from playsound import playsound
import requests
import time,re
import speech_recognition as sr
import logging

logging.getLogger("requests").setLevel(logging.WARNING)
""" 你的 APPID AK SK """
APP_ID = '17542615'
API_KEY = '4SFIsOq6PHtZRHgBuRkYdWR7'
SECRET_KEY = 'j24VY4GhyS5vscIDEP8RINI2tmHb9tdd'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
def get_audio():

    r = sr.Recognizer()
    # 麦克风
    mic = sr.Microphone(sample_rate=16000)
    # while True:
        # logging.info('录音中...')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # print(type(audio))
    audio_data = audio.get_wav_data()
    # print(type(audio_data))
    # 识别本地文件
    ret = client.asr(audio_data, 'wav', 16000, {'dev_pid': 1536, })
    # print(ret)
    if ret and ret['err_no'] == 0:
        result = ret['result'][0]
        return result

    else:
        return ret['err_msg']


def test_andio(text,filename="start"):
    result  = client.synthesis(text, 'zh', 1, {
        'spd': 6,
        'vol': 3,
    })
    # print(result)
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('{}.mp3'.format(filename), 'wb') as f:
            f.write(result)
        playsound('{}.mp3'.format(filename))
    # if not isinstance(result, dict):
    #     with open('auido.mp3', 'wb') as f:
    #         f.write(result)
    return text

def get_data (tex):
    from urllib.parse import quote
    times = str(time.time()).split('.')
    stamp = times[0]+times[1][:3]
    quote_data="{'sessionId':'a2873a71807d485c9b1e2762356a4135','robotId':'webbot','userId':'7188fb44ca6546c7b8204198023b3da0','body':{'content':'"+ str(tex) +"'},'type':'txt'}$ts=%s"%stamp
    headers={
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.98Safari / 537.36',
        'Host': 'i.xiaoi.com',
        'Cookie': 'cnonce = 626649;sig = f6d9b8b9a06624736e774d67e7afb036c530a6df;XISESSIONID = c47n6e87buz4mrf9z1294vj;Hm_lvt_b5716ef87990056024422ae4fb494926 = 1571453092;Hm_lpvt_b5716ef87990056024422ae4fb494926 = 1571453092;pgv_pvi = 2852883508;pgv_info = ssi = s5508461960;Hm_lvt_822805145daedc4d66ed5fdf3d12cc8b = 1571219830, 1571453945;Hm_lpvt_822805145daedc4d66ed5fdf3d12cc8b = 1571454035;nonce = 501041',
        'Referer': 'http://i.xiaoi.com/'
    }
    url = "http://i.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data="+quote(quote_data)
    response = requests.get(url,headers=headers)
    pattern = re.compile(r'\"fontColor\":0,\"content\":\"(.*?)\"')
    result = pattern.findall(response.text)

    print(result[0])
    return result[0].replace('\\n',"\n").replace('\\u003c',"<").replace('\\r'," ").replace('\\t'," ")


if __name__ == "__main__":
    print("hi,人工智障——对话型来了")
    while True:
        tex = get_audio()
        test_andio(text=get_data(tex))
        if (tex == "再见"):
            exit(0)
    # get_audio()



"http://i.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%27robotId%27%3A%27webbot%27%2C%27userId%27%3A%277188fb44ca6546c7b8204198023b3da0%27%2C%27sessionId%27%3A%27a2873a71807d485c9b1e2762356a4135%27%2C%27body%27%3A%7B%27" \
"content%27%3A%27None%27%7D%2C%27type%27%3A%27txt%27%7D%24ts%3D1571458850064"