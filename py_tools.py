def log(*args, **kwargs):
    print(*args, **kwargs)


def ensure(condition, message):
    # 在条件不成立的时候, 输出 message
    if not condition:
        log('*** 测试失败:', message)
    else:
        log('*** 测试成功')


def ensure_equal(a, b, message):
    if a != b:
        log('{}, ({}) 不等于 ({})'.format(message, a, b))
    else:
        log('测试成功')
