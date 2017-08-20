# -*- encoding:utf-8 -*-


print(ord('A'))  #获取对应的ASCII码
print(chr(89))   #获取对应的字符
s = 'hello'
print(s)
s1 = s.encode('utf-8')   # 将Unicode编码转换为utf-8编码
print(s1)
s2 = s1.decode('utf-8')   # 将utf-8编码转换为Unicode编码
print(s2)
value1 = "hello"
print('这是替代字符串 %s 的案例' % value1)
print('这是代替数字 %d 的案例' % 100)
print('这是替代浮点数 %f 的案例' % 3.14)
print('这是表示占位符 %？的案例')
print('这是表示十六进制 %x 的案例' % 0X1315)