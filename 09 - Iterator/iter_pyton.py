import time
import uuid
import sys

num = 10000000

start_time_for = time.time()
uuids_for = [uuid.uuid4() for _ in range(num)]
end_time_for = time.time()

size_for = sys.getsizeof(uuids_for)

start_time_iter = time.time()
uuids_iter = iter(uuid.uuid4() for _ in range(num))
end_time_iter = time.time()

size_iter = sys.getsizeof(uuids_iter)


print("Tiempo de ejecucion con 'for': ", end_time_for - start_time_for)
print("Tamanio en memoria con 'for': ", size_for)
print("Tiempo de ejecucion con 'iter': ", end_time_iter - start_time_iter)
print("Tamanio en memoria con 'iter': ", size_iter)

