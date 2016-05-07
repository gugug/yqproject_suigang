__author__ = 'kalin'
# coding=utf-8
from betweenness_centrality import *
from collections import Counter
from candidate_words import *
import os
import time


class Keyword():
    def __init__(self):
        self.poss = {}  # 词性表
        self.word_length = {}
        self.word_score = {}

    def feature(self, string_data):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, 'tag.txt')
        files = open(file_path, "r")
        file = files.readlines()
        for line in file:
            s = line.strip().split(' ')
            self.poss[s[0]] = s[1]
        po = self.poss
        candidate_words_dict, nword = CandidateWords().get_candidate_list(string_data)
        nwword_words = nword.values()  # order words
        pos = {}
        for word in nwword_words:
            self.word_length[word] = len(word) / 3
            if candidate_words_dict[word] in po.keys():
                pos[word] = float(po[candidate_words_dict[word]])
            else:
                pos[word] = 0.1
        words_tf_dict = dict(Counter(nwword_words))
        files.close()
        return (pos, words_tf_dict, self.word_length, nwword_words)

    def score(self, string_data):
        tw = 0.4
        vdw = 0.6
        lenw = 0.1
        posw = 0.5
        tfw = 0.8
        pos, words_tf_dict, word_length, candidate_word = self.feature(string_data)
        vd = BetweenCentrality().codes_betweeness_centarlity(string_data)
        for word in candidate_word:
            s = (vd[word] * vdw) + (tw * (word_length[word] * lenw + pos[word] * posw + words_tf_dict[word] * tfw))
            self.word_score[word] = s
        rank = sorted(self.word_score.iteritems(), key=lambda d: d[1], reverse=True)
        return rank

    def keyword(self, string_data):
        start = time.clock()
        key_score = self.score(string_data)
        keywords = []
        for key in key_score[0:5]:
            keywords.append(key[0])
        return keywords

    def combine_keywords(self, string_data):
        """
        提取关键字
        :param string_data: 输入文本，需要被提取的文本（string）
        :return: 提取的关键字（string）
        """
        a = self.keyword(string_data)
        combine_keywords = ''
        for i in a:
            combine_keywords += (i + ' ')
        return combine_keywords


if __name__ == "__main__":
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
