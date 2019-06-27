import hashlib
import time
from manager.models import Manager


def add(user, password):
    h = hashlib.md5()
    h.update(str(password).encode('utf-8'))
    password = h.hexdigest()
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    db = Manager(name=user, password=password, date=now, permission=1)
    # 更新数据
    db.save()


# add('root', 1996010207)
