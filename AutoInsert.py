import pymysql
from threading import Timer
import random
import datetime
'''''''''
now = datetime.datetime.now()
now.strftime('%Y-%m-%d %H:%M:%S')
print(now.strftime('%Y-%m-%d %H:%M:%S'))

def random_int_generator(below,upper):
    return random.randint(below, upper)

def random_float_generator(below,upper):
    return round(random.uniform(below, upper), 2)

print(random_int_generator(1, 4))
print(random_float_generator(50, 100))
'''''''''
count = 10
def loopfunc(msg):
    global count
    count += 1

    db = pymysql.connect('localhost', 'root', '1234', 'test')
    cursor = db.cursor()
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute(
        "insert into tb_pipe_warning_info(pipe_id,area_id,warning_level,warning_value,warning_time,warning_status) values(%d,%d,%d,%.2f,'%s',%d)" % (
        random.randint(1, 11), random.randint(1, 6), random.randint(1, 4), random.uniform(50, 100),
        now, 0))
    # print("insert into tb_pipe_warning_info(pipe_id,area_id,warning_level,warning_value,warning_time,warning_status) values(%d,%d,%d,%.2f,'%s',%d)" % (random.randint(1, 11), random.randint(1, 6), random.randint(1, 4), random.uniform(50, 100), now.strftime('%Y-%m-%d %H:%M:%S'), 0));
    db.commit()
    cursor.close()
    db.close()
    print('插入时间-->', now, '日志-->%s' % msg)
    if count != 10:
        Timer(3, loopfunc, ('插入记录%d' % count,)).start()


Timer(1, loopfunc, ('开始插入第%d条记录。' % count,)).start()




