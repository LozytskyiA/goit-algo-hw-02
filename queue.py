from queue import Queue

q = Queue()
next_id = 1

def generate_request():
    global next_id
    q.put(f"Request-{next_id}")
    next_id += 1

def process_request():
    if not q.empty():
        req = q.get()
        print("Обработка:", req)
    else:
        print("Черга пуста")

