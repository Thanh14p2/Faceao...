import os
import requests
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from threading import Lock

def clear():
    """Clear console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def check_proxy(proxy, live_prxy, die_prxy, lock):
    """Check if a proxy is live or not"""
    try:
        testing = requests.get('http://httpbin.org/ip', proxies={'http': proxy, 'https': proxy}, timeout=1).json()
        with lock:
            live_prxy[0] += 1
        with open(live_prxy[1], "a") as output_file:
            output_file.write(f"{proxy}\n")
    except:
        with lock:
            die_prxy[0] += 1

    with lock:
        print(f"\r\033[1;32mWORKING:{live_prxy[0]}  \033[1;37m|   \033[1;31mDIE:{die_prxy[0]}", end=" ")
 
def run():
    """Run the program"""
    clear()

    # Read proxies from file
    proxy_file = input('Nhập File Có Proxy:')
    proxies = list(filter(None, open(proxy_file, "r").read().split("\n")))

    # Set up output file and lock
    output_file = input('Nhập File Lưu Proxy Live: ')
    live_prxy = [0, output_file]
    die_prxy = [0]

    lock = Lock()

    # Create thread pool and submit tasks
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = []
        for proxy in proxies:
            future = executor.submit(check_proxy,proxy,live_prxy,die_prxy,lock)
            futures.append(future)

        wait(futures, return_when=ALL_COMPLETED)
 
run()
