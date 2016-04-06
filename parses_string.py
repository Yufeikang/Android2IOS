#!/usr/bin/env python3
# encoding: utf-8

"""
@version: 1.0
@author: kang
@license: Apache Licence 
@contact: kyf0722@gmail.com
@site: http://www.kangyufei.net
@software: PyCharm
@file: parses_string.py
@time: 4/5/2016 20:02
@description: 解析 xml 文件 和 IOS strings 文件
"""

import xmltodict, re


def parses_xml(filename_list=[]):
    string_dict = {}
    for filename in filename_list:
        print('parse file : %s' % filename)
        f = open(filename, 'r', encoding='utf-8')
        context = f.read()
        f.close()
        string_list = xmltodict.parse(context)["resources"]['string']
        for _dict in string_list:
            try:
                string_dict[_dict['@name']] = _dict['#text']
            except Exception as err:
                print("parses_xml ERROR: %s" % err)
    return string_dict


def parses_strings(filename=''):
    print('parse file : %s' % filename)
    string_dict = {}
    f = open(filename, 'r', encoding='utf-8')
    context = f.read()
    f.close()
    string_list = re.findall('"[\s\w\.-]+?"\s*?=\s*?"[\s\S]+?"', context)
    for s in string_list:
        [key, value] = re.findall('\"[\s\S]+?\"', s)
        key = key[1:-1].strip()
        value = value[1:-1].strip()
        string_dict[key] = value
    print("%s : num = %s" % (filename, string_dict.__len__()))
    return string_dict, context


def sync_ios_dict_to_context(ios_string_dict={}, ios_string_file_context=''):
    for k in ios_string_dict.keys():
        v = ios_string_dict[k]
        str_dict = '\"%s\" = \"%s\"' % (k, v)
        ios_string_file_context = re.sub('\"%s\"\s*?=\s*?\"[\s\S]+?\"' % k, str_dict, ios_string_file_context)
    return ios_string_file_context


if __name__ == '__main__':
    # parses_xml(['D:/DevProject/PyProject/Android2IOS/values/strings_obd2l.xml', ])
    parses_strings('C:\\Users\\kang\\Desktop\\mgr_ctrl.strings')
