# coding=utf-8
import random
from time import sleep

from get_keyword.get_keyword import *
__author__ = 'yc'
# class A():
#     def __init__(self):
#         self.a = []
#
#     def test(self):
#         b = [1,2,3,4,5]
#         c = [5,6,7,8,9]
#
#         e = []
#
#         for i in range(3):
#             print self.a
#
#             for j in c:
#                 if j not in self.a:
#                     print '不在'
#                     e.append(j)
#                 else:
#                     print "zai"
#             self.a += e
#         print self.a
#
# A().test()
# b = [1, 2, 3, 4, 5]
# c = [5, 6, 7, 8, 9]
# d = zip(b, c)
# print len(d)
# for i in range(0, len(c)):
#     print i
#     print d[i]
#     print d[i][0]
# # result_num = [1]
# # if result_num:
# #     result_num.append(1)
# # else:
# #     result_num.append(2)
# #
# # print result_num
# a= ('\xe5\x9b\xbd\xe5\x8a\xa1\xe9\x99\xa2\xe6\x8b\x9f\xe8\xa7\x84\xe5\xae\x9a\xe5\x8c\xbb\xe7\x96\x97\xe6\x9c\xba\xe6\x9e\x84\xe4\xb8\x8d\xe5\xbe\x97\xe6\x93\x85\xe8\x87\xaa\xe9\x85\x8d\xe7\x94\xa8\xe5\xa4\xa7\xe5\x9e\x8b\xe5\x8c\xbb\xe7\x94\xa8\xe8\xae\xbe\xe5\xa4\x87', '\xe5\x8c\xbb\xe7\x96\x97\xe6\x9c\xba\xe6\x9e\x84 \xe5\x9b\xbd\xe5\x8a\xa1\xe9\x99\xa2 \xe5\x8c\xbb\xe7\x94\xa8 \xe8\xae\xbe\xe5\xa4\x87 \xe9\x85\x8d\xe7\x94\xa8 \xe6\x8b\x9f \xe5\xa4\xa7\xe5\x9e\x8b ', 'M_Du0DXDZBD')
# for i in a:
#     print i
class TT():
    def __init__(self):
        self.topic = []
    def kk(self):
        self.topic = []
        strblog = [
            ' #拍案惊奇#【印尼渔民捡充气娃娃 误认为天使每天换装供奉】日前，印尼邦盖群岛一名21岁的渔夫在岸边捡到一具漂亮的女性玩偶，事情刚好发生在“日食”奇景后，村里的人便以为是“天降神灵”，每天为这个“天使”精心打扮。事件经由媒体报道惊动警方，才发现原来只是个充气娃娃。',
            '【转发收藏！18个适合毕业旅行的地方[推荐]】毕业离校的日期一天天临近，大家即将各奔东西，除了吃散伙饭、拍纪念照，在最后的告别之前，还要来一场难忘的毕业旅行！18个适合毕业旅行的地方，有辽阔的呼伦贝尔、壮丽的敦煌，也有小资青岛、梦幻迪士尼...戳图选择↓↓青春回忆，别给明天留遗憾！[心]',
            '【心酸！下井前后夫妻照，矿工判若两人】3日，安徽淮北，一座煤矿上夜班的煤矿工人上井后，穿着工作服、头戴矿灯，每人与妻子拍一张图片。之后，煤矿工人去澡堂洗澡；洗澡结束后，换上干净的服装，每人再与妻子拍一张图片。之前之后，矿工判若两人↓↓via视觉中国',
            ' #小夏推荐# 【TED演讲】说出感谢。在这看似简单的3分钟的谈话中，Laura Trice 博士告诉你“谢谢你”这句话具有的神奇力量。有时候你和他之间的隔阂可能只差一句赞美。试试吧。秒拍视频',
            '【中国大陆最富500人出炉 王健林王思聪登顶】《新财富》杂志发布中国大陆最富500人排行榜，万达集团董事长王健林、王思聪父子合计财富达人民币1982.6亿元，重返第一宝座。前500名的富人拥有的财富总额达到80191.5亿元，人均财富达160.4亿元，百亿富豪达302位，比去年增加了8成。中国富豪榜:王健林王思聪登顶 ',
            '【4岁自闭症儿童殒命康复机构 死前1天拉练19公里】4岁的自闭症儿童嘉嘉被妈妈送至广州的一家自闭症康复机构接受康复训练。机构称为慢性病康复探索着一条新路…采用“全封闭、军事化管理”，每月学费10400元。4月27日，妈妈被告知孩子死亡。监控表显示，死前1天孩子被拉练19公里。每天穿棉衣拉练一二十公里 3岁自闭症男童死在康复基地',
            ' #五四青年节#纪念1919年5月4日，“五•四”运动爆发。对星战迷因为在《星球大战》系列中有一句非常著名的台词“May the force be with you(原力与你同在)”，而5月4号用英文说就是“May the fourth”，与前面的台词发音相同，所以今天就又被星战迷称为星战日了。五四青年节/星战日快乐！',
            ' #民调时间#【魏则西之死，你认为最主要责任是？】大学生魏则西，因身患滑膜肉瘤去世。其生前求医过程中，通过百度搜索看到排名前列的武警北京总队第二医院，受其鼓吹的疗法所骗，花费二十多万元无济于事，也贻误了其他合理治疗的时机。对于他的死，你认为责任在谁？ #魏则西事件#  '
        ]
        for i in strblog:
            a = Keyword().combine_keywords(i)
            print strblog.index(i),a
            if a not in self.topic:
                self.topic.append(a)
        print len(self.topic)

    def acc(self):
        account = {
                "人民日报": 2803301701, "新浪新闻": 2028810631, "凤凰周刊": 1267454277,
                "网易新闻客户端": 1974808274, "北京晨报": 1646051850,
                "头条新闻": 1618051664, "人民网": 2286908003,
                "财经网": 1642088277, "新京报": 1644114654, "环球时报": 1974576991,
                "中国新闻网": 1784473157, "三联生活周刊": 1191965271, "法制晚报": 1644948230,
                "新闻晨报": 1314608344, "中国之声": 1699540307, "中国新闻周刊": 1642512402,
                "澎湃新闻": 5044281310, "中国日报": 1663072851, "北京青年报": 1749990115,
                "新快报": 1652484947, "华西都市报": 1496814565, "凤凰网": 2615417307,
                "FT中文网": 1698233740,
        }
        rand_account = random.sample(account,6)  # 从 account 中随机获取5个元素，作为一个片断返回
        print type(rand_account)
        for i in rand_account:
            print i, account[i]

    def auto_run(self):
        while True:
            self.kk()
            self.acc()
            sleep(2)
            print "睡醒"


tt = TT()
tt.auto_run()
