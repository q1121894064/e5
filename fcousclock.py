import time

# 设置专注时间（以秒为单位）
focus_time = 25 * 60

# 倒计时
while focus_time:
    # 将秒数转换为分钟和秒钟
    mins, secs = divmod(focus_time, 60)

    # 格式化剩余时间并输出
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")

    # 等待1秒
    time.sleep(1)

    # 减少剩余时间
    focus_time -= 1

# 专注时间结束后播放声音或给出提醒
print('时间到！')
