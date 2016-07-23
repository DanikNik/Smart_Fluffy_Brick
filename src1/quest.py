#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
#################################################################################
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

		ans = ans.lower()
##!Осторожно! Говнокод!!!
		ans = ans.replace(" i ", " первый ")
		ans = ans.replace(' ii ', ' второй ')
		ans = ans.replace(' iii ', ' третий ')
		ans = ans.replace(' iv ', ' четвёртый ')
		ans = ans.replace(' v ', ' пятый ')
		ans = ans.replace(' vi ', ' шестой ')
		ans = ans.replace(' vii ', ' седьмой ')
		ans = ans.replace(' viii ', ' восьмой ')
		ans = ans.replace(' iix ', ' восьмой ')
		ans = ans.replace(' ix ', ' девятый ')
		ans = ans.replace(' x ', ' десятый ')
		ans = ans.replace(' xi ', ' одиннадцатый ')
		ans = ans.replace(' xii ', ' двенадцатый ')
		ans = ans.replace(' xiii ', ' тринадцатый ')
		ans = ans.replace(' xiv ', ' четырнадцатый ')
		ans = ans.replace(' xv ', ' пятнадцатый ')
		ans = ans.replace('(', '')
		ans = ans.replace(')', '')
		ans = ans.replace('англ.', '')
		ans = ans.replace('фран.', '')
		ans = ans.replace('франц.', '')
		if qi > 0:
			ans = "Возможно, вы имели ввиду "+ans
		return ans
	except:
		ans = "Я вас не понял, перефразируйте запрос"
		return ans
#################################################################################
def WhatIs(text, text_arr):
	url = ""
	try:
		mi = text_arr.index('такая') + 1
	except:
		try:
			mi = text_arr.index('такой') + 1
		except:
			try:
				mi = text_arr.index('такое') + 1
			except:
				try:
					mi = text_arr.index('такие') + 1
				except:
					mi = text_arr.index('значит') + 1
	mi1 = mi
	while mi1 < len(text_arr):
		if mi1 > mi:
			url += " "
		url += str(text_arr[mi1])
		mi1 += 1
	ans = GetThingQuest(url)
	return ans
#################################################################################
def Trans(text, lang):
	langs = {'русский':'ru','английский':'en'}
	try:
		mi = text.find("переведи на ")
		a = list(langs.keys()).index(lang)
		mi = mi + len(list(langs.keys())[a]) + 12
		text = text[mi:]
		lang = langs.get(lang)
		ans = requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate', data={'key':'trnsl.1.1.20160723T075443Z.3071860cf4a85efc.3fef18c09d8253d502944581b4360833ed8749f2','lang':lang,'text':text}).json()
		ans = ans['text'][0]
	except:
		ans = "Данный язык недоступен. Доступные языки: "+str(list(langs.keys()))
	return ans
#################################################################################
text = input()##Способ общения: input или open
l_text = text.lower()
arr_l_text = l_text.split()
#################################################################################
if (arr_l_text[0] == "переведи") or (arr_l_text[1] == "переведи"):
	lang = arr_l_text[2]
	ans = Trans(l_text, lang)
elif (arr_l_text[0] == "вопрос") or (arr_l_text[1] == "вопрос"):
	if (l_text.find('кто такой') != -1) or (l_text.find('кто такая') != -1) or (l_text.find('кто такое') != -1) or (l_text.find('что такое') != -1) or (l_text.find('кто такие') != -1) or ((l_text.find('что значит')) != 1):
		ans = WhatIs(l_text, arr_l_text)
else:
	ans = FreeQuest(arr_l_text, arr_l_text)
print(ans)