#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests, re
from bs4 import BeautifulSoup

#def NameBadRequest()#План "средниум"

def BadRequest():###Пока что так! -- план минимум
	ans = "Пожалуйста, перефразируйте запрос"

def GetQuest():
	global url_text
	#print(url_text)
	#url = 'https://duckduckgo.com?q='+url_text+'&format=json&ia=about'
	#print(url)
	ans = requests.post('https://duckduckgo.com', data={'q':url_text,'format':'json', 'ia':'about'})
	#print(ans.url)
	#print(ans.text)
	ans = ans.text
	parsed = BeautifulSoup(ans)
	#print("!!!",parsed)
	topics = parsed.findAll('div', {'id':'zci-about'})#[0][0][0][1]
#	topic = topic.findAll('div', {'class':'c-info--cw  cw has-aux'})
#	topic = topic.findAll('div', {'class':'czi-main  c-info'})
#	topic = topic.findAll('div', {'class':'czi-body'})
#	topic = topic.findAll('div', {'class':'c-info__body'})
	ans = topics.findAll('div', {'class': re.compile('results_*')})
	ans = ans[1].text
	print(topic)
	print("\n\n", ans)
	if len(ans) <= 5:
		BadRequest()
	return ans

def ChtoTakoe():
	global l_text, arr_l_text, url_text
	url_text = ""
	mi = arr_l_text.index('такое') + 1
	mi1 = mi
	while mi1 < len(arr_l_text):
		if mi1 > mi:
			url_text += " "
		url_text += str(arr_l_text[mi1])
		mi1 += 1
	ans = GetQuest()
	return ans

#def KtoTakoi(): #План "средниум"
#	global l_text, arr_l_text, url_text



text = input()##Способ общения: input или open
l_text = text.lower()
arr_l_text = l_text.split()
url_text = ""

if l_text.find('что такое') != -1:
	ans = ChtoTakoe()
elif (l_text.find('кто такой') != -1) or (l_text.find('кто такая') != -1):
	#План "средниум -- "KtoTakoi(l_text, arr_l_text)
	ans = ChtoTakoe()
else:
	SomeWhat()####!!!!!Не готово

print("\n====================ANSWER==================\n"+ans)
