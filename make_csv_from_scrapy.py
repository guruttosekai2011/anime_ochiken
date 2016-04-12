#coding: UTF8

import sys
import urllib2
import lxml.html
from bs4 import BeautifulSoup

import codecs
import MySQLdb as mysql


def scrape():

    hall_list = []

    url = "http://animetranscripts.wikispaces.com/Code+Geass+%3E+2.+The+White+Knight+Awakens"
    #print url
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html)

    _dic = {}
    scene = 0

    for comments in soup.find_all("div", class_="commentContainer"):

        for items in comments.find_all("span"):

            for item in items.find_all("span"):

                if "----------" in unicode(item):
                    scene += 1
                    s_key = "scene" + str(scene)
                    _dic.update({s_key:{}})

                    #print ""
                    #print unicode(item.string) 

                else:
                    uni = unicode(item)
                    if "strong" in uni:
                        for it in item.find_all("strong"):

                            talker = it.string.replace(":", "").replace(" ", "")
                            if not _dic[s_key].has_key(talker):
                                _dic[s_key].update({talker:[]})

                            #print ""
                            #print it.string,
                    else:
                        speak = uni.split(">")[1].split("<")[0]
                        if scene != 0:
                            _dic[s_key][talker].append(speak)

                            #print uni.split(">")[1].split("<")[0],

    for s_key in _dic.keys():
        print s_key
        print "talkers:"
        print _dic[s_key].keys()
        print ""
        for key in _dic[s_key]:
            print key + ":",
            print _dic[s_key][key]

        print ""
        print ""

    return s_key,_dic


def make_csv(s_key,_dic):

    print s_key
    print _dic

    return


if __name__ == '__main__':

    s_key,_dic = scrape()
    make_csv(s_key,_dic)

