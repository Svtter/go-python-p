import ctypes

lib = ctypes.cdll.LoadLibrary('/Users/xiuhao/work/explore/go-python-p/demo.so')

result = lib.add(2020, 1)
print('add: ', result)

content = b"""{"code": 1, "msg": "success", "data": "hello"}"""
p = ctypes.create_string_buffer(content)
print('parse: ', result)
