"""
Copyright © 时趣互动（北京）科技有限公司
@contact: wujianqiang@social-touch.com
@file: String.py
@time: 16/6/15 下午12:58
@desc: 
"""
class String(object):
    """
    提供一些字符串处理的工具
    """

    @staticmethod
    def is_chinese(uchar):
        """
        判断一个unicode是否是汉字
        :param uchar:
        :return:
        """
        if u'\u4e00' <= uchar <= u'\u9fa5' \
                or u'\u9fa6' <= uchar <= u'\u9fcb' \
                or u'\u3400' <= uchar <= u'\u4db5' \
                or u'\u20000' <= uchar <= u'\u2a6d6' \
                or u'\u2a700' <= uchar <= u'\u2b734' \
                or u'\u2b740' <= uchar <= u'\u2b81d' \
                or u'\u2f00' <= uchar <= u'\u2fd5' \
                or u'\u2e80' <= uchar <= u'\u2ef3' \
                or u'\uf900' <= uchar <= u'\ufad9' \
                or u'\u2f800' <= uchar <= u'\u2fa1d' \
                or u'\uE815' <= uchar <= u'\uE86F' \
                or u'\uE400' <= uchar <= u'\uE5E8' \
                or u'\u31C0' <= uchar <= u'\u31E3' \
                or u'\uE600' <= uchar <= u'\uE6CF' \
                or u'\u3105' <= uchar <= u'\u3120' \
                or u'\u31A0' <= uchar <= u'\u31BA' \
                or u'\u2FF0' <= uchar <= u'\u2FFB':
            return True
        else:
            return False

    @staticmethod
    def is_number(uchar):
        """
        判断一个unicode是否是数字
        :param uchar:
        :return:
        """
        if 48 <= ord(uchar) <= 57:
            return True
        else:
            return False

    @staticmethod
    def is_alphabet(uchar):
        """
        判断一个unicode是否是英文字母
        :param uchar:
        :return:
        """
        if 65 <= ord(uchar) <= 90 or 97 <= ord(uchar) <= 122:
            return True
        else:
            return False

    @staticmethod
    def is_special(uchar):
        """
        判断一个unicode是否是特殊字符
        :param uchar:
        :return:
        """
        if ord(uchar) <= 47 or 58 <= ord(uchar) <= 64 or 91 <= ord(uchar) <= 96 or 123 <= ord(uchar) <= 127:
            return True
        else:
            return False

    @staticmethod
    def form_code(string):
        """
        返回字符串构成编码,主要为纯中文、纯英文、纯属字、纯其他字符、以及四种的各类组合
        :param string:
        :return:返回四位长度的编码,从0000~1111,从左往右依次表示是否含有中文、英文、数字、其他字符,如1000表示纯中文字符串
        """
        schema = {
            'zh': '0',
            'en': '0',
            'num': '0',
            'other': '0'
        }
        for uchar in string:
            if String.is_chinese(uchar):
                schema['zh'] = '1'
                continue
            if String.is_number(uchar):
                schema['num'] = '1'
                continue
            if String.is_alphabet(uchar):
                schema['en'] = '1'
                continue
            schema['other'] = '1'

        return schema['zh'] + schema['en'] + schema['num'] + schema['other']