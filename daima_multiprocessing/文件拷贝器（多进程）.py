import os,random,time
import multiprocessing


def copy_file(queue, file_name,source_f_name, dest_f_name):
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
    queue.put(file_name)

def main():
    sourcez_f_name = input("Pelease input folder name")
    dest_f_name = sourcez_f_name + '[复件]'
    # 创建目标文件夹
    try:
        os.mkdir(dest_f_name)
    except:
        pass

    file_names = os.listdir(sourcez_f_name)

    queue = multiprocessing.Manager().Queue()

    pool = multiprocessing.Pool(3)

    for file in file_names:
        pool.apply_async(copy_file,args=(queue,file,sourcez_f_name,dest_f_name))

    pool.close()

    #显示进度条
    all_f_num = len(file_names)
    while True:
        file_name = queue.get()
        if file_name in file_names:
            file_names.remove(file_name)

        copy_rate = (all_f_num - len(file_names))*100/all_f_num
        print('\rworing%.1f' % copy_rate)
        if copy_rate >= 100:
            break
    print()



if __name__ == '__main__':
    main()



