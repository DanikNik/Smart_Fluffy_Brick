#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests, re

#def NameBadRequest()#План "средниум"

def BadRequest(ans):###Пока что так! -- план минимум
	ans = "Пожалуйста, перефразируйте запрос"

def GetQuest(request):
	for i in range(len(requests.post('https://ru.wikipedia.org/w/api.php', data={'action':'opensearch', 'search':request, 'format':'json'}).json())):
		ans = (requests.post('https://ru.wikipedia.org/w/api.php', data={'action':'opensearch', 'search':request, 'format':'json'}).json())[2][i]
		if len(ans) > 21:
			qi = i
			break
	bb = 0
	eb = 0
	todel = ""
	for i in ans:
		#print(i, bb, eb, todel)
		if i == "(":
			bb += 1
		elif i == ")":
			eb += 1
		if bb > 0:
			todel += i
		if (bb == eb) and (bb > 0):
			ans = ans.replace(todel, "")
			todel = ""
			bb = 0
			eb = 0

	print(ans)
	if len(ans) < 5:
		ans = BadRequest(ans)
	else:
		if qi > 0:
			ans = "Возможно, вы имели ввиду "+ans
	return ans


def ChtoTakoe(text, text_arr, url):
	url = ""
	mi = text_arr.index('такое') + 1
	mi1 = mi
	while mi1 < len(text_arr):
		if mi1 > mi:
			url += " "
		url += str(text_arr[mi1])
		mi1 += 1
	ans = GetQuest(url)
	return ans

#def KtoTakoi(): #План "средниум"
#	global l_text, arr_l_text, url_text



text = input()##Способ общения: input или open
l_text = text.lower()
arr_l_text = l_text.split()
url_text = ""

if l_text.find('что такое') != -1:
	ans = ChtoTakoe(l_text, arr_l_text, url_text)
elif (l_text.find('кто такой') != -1) or (l_text.find('кто такая') != -1):
	#План "средниум -- "KtoTakoi(l_text, arr_l_text)
	ans = ChtoTakoe()
else:
	SomeWhat()####!!!!!Не готово

print("\n====================ANSWER==================\n"+ans)
