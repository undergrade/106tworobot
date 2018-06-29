# 106TwoBoT
106年專題---兩台機器人避障系統，老鷹抓小雞

使用q-learning演算法，讓turtlebot學習如何躲過障礙物，並將turtlebot在虛擬中的移動方式同步傳送給現實中的turtlebot;而當turtlebot靠近並辨識到令一台turtlebot時，便會停止前進。

環境安裝
請參閱https://github.com/erlerobot/gym-gazebo/blob/master/INSTALL.md
(不要git clone此網站 git clone原文即可)
遇到問題可參考https://blog.csdn.net/zhangdadadawei/article/details/78906103

執行
cd gym-gazebo/examples/turtlebot/
roslaunch minimal.launch
再開令一個視窗
python cascade.py
再開令一個視窗
python3 test2

可再開令一個視窗
輸入
gzclient
即可觀察turtlebot在gazebo中的移動

將test2.py中的

#    file = open("qtable.dat", "wb")
                
#    pickle.dump(qlearn.q,file)

            
#    file.close()

都去掉＃可讓每次training的q-table傳給下次training。
