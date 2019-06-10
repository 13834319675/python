movie_list = ["斗破.mp4", "复仇者联盟.avi","钢铁雨.rmvb","xxx.mp4"]
music_list = ['周杰伦.mp3','五月天.mp3']
movie_format = ['mp4','avi']
music_format = ['mp3']
import threading
import time

def play(playlist):
    for i  in  playlist:
        if i.split(".")[1] in movie_format:
            print("正在播放的是:{}".format(i))
            time.sleep(2)

        elif i.split(".")[1] in music_list:
            print("正在播放的是:{}".format(i))
            time.sleep(3)
        else:
            print("没有合适的格式")

def thread_run():
    t1 = threading.Thread(target=play,args=(movie_list,))
    t2 = threading.Thread(target=play,args=(music_list,))
    t1.start()
    t2.start()

if __name__ == '__main__':
    thread_run()