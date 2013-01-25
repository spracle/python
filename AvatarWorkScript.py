# _*_ coding:utf-8 _*_

import os 
import os.path 
import shutil 

targetDir = r"E:\kk2\bin\client\UIDataFiles\imagesets"
sourceFile1 = r"F:\PVE_2.png"
sourceFile2 = r"F:\PVE_2.jpg"

def ReplaceUILayout():
	for file in os.listdir(targetDir):
	  targetFile = os.path.join(targetDir,file)
	  if os.path.isfile(targetFile) and targetFile.find(".png") > 0: 
	    open(targetFile, "wb").write(open(sourceFile1, "rb").read())
	  if os.path.isfile(targetFile) and targetFile.find(".jpg") > 0:
	  	open(targetFile, "wb").write(open(sourceFile2, "rb").read())


def CopyDllToDir():
	shutil.copyfile(r"E:\kk2\code\contrib\gperftools\Release\libtcmalloc_minimal.dll", r"E:\kk2\bin\client\libtcmalloc_minimal.dll")
	shutil.copyfile( r"E:\kk2\code\contrib\gperftools\Release\libtcmalloc_minimal.lib", r"E:\kk2\code\contrib\lib\libtcmalloc_minimal.lib")
	#shutil.copyfile( r"E:\kk2\code\contrib\MemeryLog\Release\MemeryLog.dll", r"E:\kk2\bin\client\MemeryLog.dll")
	#shutil.copyfile( r"E:\kk2\code\contrib\MemeryLog\Release\MemeryLog.lib", r"E:\kk2\code\contrib\lib\MemeryLog.lib")


def RecordUILayoutNameToFile():
	sourceDir = r"E:\kk2\bin\client\UIDataFiles\layouts"
	f = open("aaLayoutFiles.txt","w")
	for file in os.listdir(sourceDir):
		f.write(file)
		f.write("\n")
	f.close()

if __name__ == "__main__":
	rets = []
	for val in map(lambda x:int(x),raw_input().split(',')):
		for ret in range(10 ** val-1,0,-1):
			if ret % val == 0:
				rets.append(ret)
				break
	print ",".join(map(lambda x:str(x),rets))

	input()


