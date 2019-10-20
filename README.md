# pyri
Artificial mental retardation
实在无聊，动手写了人工智障实现简易版siri。
调用百度的语音识别与合成的接口实现了语音的输入与输出。
主要的对话机器人方面是利用爬虫模拟爬取的小i(i.xiaoi.com)
还有很多细节待优化。以后闲下来再写吧。


###注：
playsound无法主动释放内存,导致只能播放一次，产生的mp3文件不能覆盖，
需要改动一些源码。
再此提供一种简单的修改方法：
我使用的是win + pycharm所产生的虚拟环境，按自己的环境自行修改。
####项目路径\venv\Lib\site-packages\playsound.py
大概40行的位置
    if block:
        sleep(float(durationInMS) / 1000.0)
        winCommand('close', alias)#增加此行代码