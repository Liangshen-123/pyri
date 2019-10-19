import wx
import test
import uide
import re
from threading import Thread


class CalcFrame(uide.MyFrame1,Thread):
    def __init__(self, parent):
        uide.MyFrame1.__init__(self, parent)
        Thread.__init__(self)
        self.start()
    def dead_xun(self):
        while True:
            tex = test.get_audio()
            self.m_textCtrl16.SetValue(str(tex))
            self.Update()
            res = str(test.get_data(tex)).replace("{br}", "。\n").replace(" ", "")
            resa = re.sub(u"\\(.*?\\)|\\{.*?\\}|\\[.*?\\]", "", res)
            print(resa)
            self.m_textCtrl5.SetValue(str(resa))
            self.Update()

            test.test_andio(text=resa)
            if (tex == "再见"):
                exit(0)
    # 按键事件触发函数
    # def my_submit(self, event):
    #     super(CalcFrame, self).my_submit(event)
    #     # thread_obj = threading(self.dead_xun())
    #     # thread_obj.start()
    #     self.dead_xun()
    def run(self):
        self.dead_xun()



def main():
    app = wx.App(False)
    frame = CalcFrame(None)
    frame.Show(True)
    # start the applications
    app.MainLoop()



if __name__ == '__main__':
    main()

