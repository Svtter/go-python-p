import ctypes

lib = ctypes.cdll.LoadLibrary('/Users/xiuhao/work/explore/go-python-p/libdemo.so')

result = lib.add(2020, 1)
print('add: ', result)

# 调用go模块
go_append_str = lib.append_str

# 显式声明参数和返回的期望类型
go_append_str.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
go_append_str.restype = ctypes.c_char_p
result_bytes = go_append_str("测试".encode("utf-8"),'数据'.encode("utf-8"))
result = result_bytes.decode("utf-8")
print(result)

content = """{"code": 1, "msg": "success", "data": "hello"}"""
# p = ctypes.create_string_buffer(content)

go_parse_JSON = lib.parseJSON
go_parse_JSON.argtypes = [ctypes.c_char_p]
go_parse_JSON.restype = ctypes.c_char_p
result_bytes = go_parse_JSON(content.encode('utf-8'))
result = result_bytes.decode("utf-8")
print(result)