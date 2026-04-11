

def info(msg):
    print('[提示]'+msg)

def warn(msg):
    print('[警告]'+msg)

def error(msg):
    print('[错误]'+msg)

def log(func, text):
    func(text)

log(info, '成功添加')
log(warn, '输入有误')
log(error, '执行报错')