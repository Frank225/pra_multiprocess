oldname = input("please input name!")

oldfile = open(oldname,'r')
houzhui = oldname.rfind(".")
if houzhui > 0:
    houzhui_name = oldname[houzhui:]
qianzhui_name = oldname[0:houzhui]
newname = qianzhui_name + '[附件]' + houzhui_name

newfile = open(newname,'w')

contents = oldfile.readlines()
for content in contents:
    newfile.write(content)

oldfile.close()
newfile.close()
