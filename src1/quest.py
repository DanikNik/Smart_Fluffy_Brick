#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests, re
#from bs4 import BeautifulSoup as htmlsoup

#def NameBadRequest()#План "средниум"

def GetThingQuest(request):
	try:
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

		#print(ans)
		if qi > 0:
			ans = "Возможно, вы имели ввиду "+ans
		return ans
	except:
		ans = "Я вас не понял, перефразируйте запрос"
		return ans

def WhatIs(text, text_arr):
	url = ""
	try:
		mi = text_arr.index('такая') + 1
	except:
		try:
			mi = text_arr.index('такой') + 1
		except:
			mi = text_arr.index('такое') + 1
	mi1 = mi
	while mi1 < len(text_arr):
		if mi1 > mi:
			url += " "
		url += str(text_arr[mi1])
		mi1 += 1
	ans = GetThingQuest(url)
	return ans

def GetFreeQuest(request):
	print(href)

def FreeQuest(text, text_arr):
	url = ""
	for i in range(len(text_arr) - 1):
		if i != 0:
			if i != len(text_arr) - 1:
				url += text_arr[i]+" "
			else:
				url += text_arr[i]
	ans = GetFreeQuest(url)


text = input()##Способ общения: input или open
l_text = text.lower()
arr_l_text = l_text.split()

if arr_l_text[0] == "вопрос":
	if (l_text.find('кто такой') != -1) or (l_text.find('кто такая') != -1) or (l_text.find('кто такое') != -1) or (l_text.find('что такое') != -1):
		ans = WhatIs(l_text, arr_l_text)
	else:
		ans = "Неверная форма вопроса."
elif arr_l_text[0] == "поищи":
	ans = FreeQuest(l_text, arr_l_text)

print("\n====================ANSWER==================\n"+ans)
