# -*- coding: utf-8 -*-
def match(f = 'dic',openFrom = "source",saveTo = "save"):
	demoFile = open(openFrom).read().decode('utf-8')
	saveFile = open(saveTo,'a')
	Dic = open(f).readlines()
	dic = {}
	for line in Dic:
		temp = line.split('*')
		words,spelling = temp[0].decode('utf-8'), temp[1].rstrip()
		dic.update({}.fromkeys(words, spelling))
	for character in demoFile:
		tem =  dic.get(character)
		if(tem!=None):
			saveFile.write(tem+" ")
			print character.encode('utf-8')," ",tem,
		else:
			saveFile.write(character.encode('utf-8'))
			print character.encode('utf-8')
	saveFile.close()
