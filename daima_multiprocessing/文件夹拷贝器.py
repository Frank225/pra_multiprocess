import os,random,time


def copy_file(file_name,source_f_name, dest_f_name):
    """copy文件到指定路径"""
    f_read = open(source_f_name + '/'+file_name,'rb')
    f_write = open(dest_f_name+'/'+file_name,'wb')
    while True:
        time.sleep(random.random())
        content = f_read.read(1024)
        if content:
            f_write.write(content)
        else:
            break
    f_read.close()
    f_write.close()

def main():
    sourcez_f_name = input("Pelease input folder name")
    dest_f_name = sourcez_f_name + '[复件]'
    # 创建目标文件夹
    try:
        os.mkdir(dest_f_name)
    except:
        pass

    file_names = os.listdir(sourcez_f_name)
    for file in file_names:
        copy_file(file,sourcez_f_name,dest_f_name)

if __name__ == '__main__':
    main()



