# 使用多线程去播放两个播放列表，一个是movie，一个是music
# - _thread
# - threading
import _thread as thread
import time


movie_list = ["斗破.mp4", "复仇者联盟.avi","钢铁雨.rmvb","xxx.mp4"]
music_list = ['周杰伦.mp3','五月天.mp3']
movie_format = ['mp4','avi']
music_format = ['mp3']

def play(playlist):
    for i  in  playlist:
        if i.split(".")[1] in movie_format:
            print("现在我们正在播放{}".format(i))
            time.sleep(2)

        elif i.split(".")[1] in music_format:
            print("现在正在播放{}".format(i))
            time.sleep(3)
        else:
            print("现在什么都没在播放,没有播放的格式")

# 启动多线程
def thread_run():
    thread.start_new_thread(play,(movie_list,))
    thread.start_new_thread(play,(music_format,))

if __name__ == '__main__':
    thread_run()
