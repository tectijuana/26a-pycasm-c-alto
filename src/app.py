import ctypes
import numpy as np

lib = ctypes.CDLL("./build/libops.so")

lib.c_suma_array.argtypes = [ctypes.POINTER(ctypes.c_long), ctypes.c_long]
lib.c_suma_array.restype = ctypes.c_long

lib.c_contar_pares.argtypes = [ctypes.POINTER(ctypes.c_long), ctypes.c_long]
lib.c_contar_pares.restype = ctypes.c_long

lib.c_dot.argtypes = [
    ctypes.POINTER(ctypes.c_long),
    ctypes.POINTER(ctypes.c_long),
    ctypes.c_long
]
lib.c_dot.restype = ctypes.c_long

arr = np.array([1,2,3,4,5,6], dtype=np.int64)
arr2 = np.array([1,1,1,1,1,1], dtype=np.int64)

ptr = arr.ctypes.data_as(ctypes.POINTER(ctypes.c_long))
ptr2 = arr2.ctypes.data_as(ctypes.POINTER(ctypes.c_long))

print("Suma:", lib.c_suma_array(ptr, len(arr)))
print("Pares:", lib.c_contar_pares(ptr, len(arr)))
print("Dot:", lib.c_dot(ptr, ptr2, len(arr)))
import time

def python_sum(arr):
    s = 0
    for x in arr:
        s += x
    return s

N = 1000000
arr_big = np.arange(N, dtype=np.int64)
ptr_big = arr_big.ctypes.data_as(ctypes.POINTER(ctypes.c_long))

# Python
start = time.perf_counter()
python_sum(arr_big)
end = time.perf_counter()
print("Python tiempo:", end - start)

# ASM
start = time.perf_counter()
lib.c_suma_array(ptr_big, N)
end = time.perf_counter()
print("ASM tiempo:", end - start)
