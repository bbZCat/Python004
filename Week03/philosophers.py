
################################################################################################################################################
# 哲学家就餐问题 MUD版 Ver 1.0                                                                                                                    #
# By ZCat 2020.10.08                                                                                                                           #
################################################################################################################################################
import threading
from multiprocessing.dummy import Pool as ThrdPool
import queue
from collections import Counter
from time import sleep, time
import random
import os
import sys

folks = [True]*5
philosophers = ("泰勒斯", "毕达哥拉斯", "苏格拉底", "柏拉图", "亚里士多德")
#定义每个人右手和左手的叉子序号
philosopherfolks = {"泰勒斯":(0, 1), "毕达哥拉斯":(1, 2), "苏格拉底":(2, 3), "柏拉图":(3, 4), "亚里士多德":(4, 0)}

def run(pname, pfolks):
    pname = "【" + pname + "】"
    print(pname +  "走进了餐厅，在正中央的大圆桌旁坐了下来。")
    #等待线程启动完成
    sleep(2)

    RFolk = pfolks[0]
    LFolk = pfolks[1]
    isRFolk = False
    isLFolk = False
    eattimes = 0
    while eattimes < goals:
        #需要休眠，否则会造成进程独占
        sleep(1)
        lock.acquire()
        try: 
            #统计可用的叉子数
            sparefolk = Counter(folks)[True]

            #只有一把空闲叉子，且自己手中无叉子时略过
            if sparefolk == 1 and not isRFolk and not isLFolk:
                print(pname + " " + random.choice(("缓缓", "茫然", "猛然")) + "抬起头...")
                print("【侍女】 " + random.choice(("不安地", "微笑着", "礼貌地", "惶恐地")) + "打断了" + pname + "，说道：不，先生，你不饿。")
            #获取所需叉子
            #如果手里没有叉子，随机拿左或者右
            elif not isRFolk and not isLFolk:
                if random.randint(0,1):
                    if folks[RFolk]:
                        print(pname + " 右手拿起了叉子...")
                        queue.put([pname, "右", "拿"])
                        folks[RFolk] = False
                        isRFolk = True
                    else:
                        print(pname + " 举起了右手，却尴尬的悬在了半空...")
                        #sleep(random.randint(1,3))
                else:
                    if folks[LFolk]:
                        print(pname + " 左手拿起了叉子...")
                        queue.put([pname, "左", "拿"])
                        folks[LFolk] = False
                        isLFolk = True
                    else:
                        print(pname + " 举起了左手，却尴尬的悬在了半空...")
                        #sleep(random.randint(1,3))
            #如果没有右叉子(只有左叉子)
            elif not isRFolk:
                if folks[RFolk]:
                    print(pname + " 右手拿起了叉子...")
                    queue.put([pname, "右", "拿"])
                    folks[RFolk] = False
                    isRFolk = True
                else:
                    print(pname + " 举起了右手，却尴尬的悬在了半空...")
                    #sleep(random.randint(1,3))
            #如果没有左叉子（只有右叉子）
            elif not isLFolk:
                if folks[LFolk]:
                    print(pname + " 左手拿起了叉子...")
                    queue.put([pname, "左", "拿"])
                    folks[LFolk] = False
                    isLFolk = True
                else:
                    print(pname + " 举起了左手，却尴尬的悬在了半空...")
                    #sleep(random.randint(1,3))
            #两个叉子都有
            else:
                print(pname + " 埋下头，" + random.choice(("狼吞虎咽", "优雅地","心不在焉地")) + "吃了起来...")
                #sleep(random.randint(2,5))
                queue.put([pname, "", "吃"])
                queue.put([pname, "右", "放"])
                queue.put([pname, "左", "放"])
                folks[RFolk] = True
                folks[LFolk] = True
                isRFolk = False
                isLFolk = False
                eattimes += 1
                msg_eaten = pname + " 深深呼出一口气，放下了手中的叉子，" + random.choice(("喃喃地说：", "自言自语道：", "心满意足道："))
                msg_eaten += f"这是我今天吃的第 {eattimes} 顿饭"
                if eattimes == goals:
                    msg_eaten += ", 终于有了饱的感觉。"
                else:
                    msg_eaten += "。"
                print(msg_eaten)
        finally:
            lock.release()

if __name__ == '__main__':
    #进餐次数
    goals = 3
    lock = threading.Lock()
    pool = ThrdPool(5)
    queue = queue.Queue()

    for i in range(5):
        params = (philosophers[i], philosopherfolks[philosophers[i]])
        pool.apply_async(run, args=(params))
    pool.close()
    pool.join()
    print("【-我-】最终，所有的哲学家都吃饱了，鼓掌~~~")
    pool.terminate()

    queue.task_done()
    with open('./Result.txt', 'a+', encoding='utf-8') as result:
        for _ in range(queue.qsize()):
            result.write(str(queue.get())+ "\n")    
        result.close()
    