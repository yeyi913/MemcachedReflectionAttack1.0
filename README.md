# MemcachedReflectionAttack1.0
该代码实现了一种基于 Memcached 的反射攻击，它利用了 Memcached 服务器的 UDP 协议中的某些漏洞。
攻击者可以伪造源 IP 地址向一个开放的 Memcached 服务器发送一个带有攻击负载的 UDP 数据包，然后服务器将响应数据包发送回伪造的源 IP 地址。
由于反射数据包的长度通常比攻击数据包长得多，因此攻击者可以使用较少的网络带宽来对目标进行攻击。
此外，攻击者还可以通过向服务器发送大量的攻击请求来放大反射数据包的大小，进一步增加攻击的威力。
该代码使用了 Shodan API 搜索公开的 Memcached 服务器列表，然后使用多线程的方式对目标 IP 进行攻击。攻击参数包括目标 IP、目标端口号、攻击线程数、攻击持续时间和反射放大倍数等。
在攻击过程中，代码会不断打印攻击数据，直到攻击结束
请注意必须把"YOUR_API_KEY"切换为shodan升级版的API

This code implements a reflection attack based on Memcached, which exploits certain vulnerabilities in the UDP protocol of the Memcached server.

Attackers can forge the source IP address and send a UDP packet with attack payload to an open Memcached server, which then sends the response packet back to the forged source IP address.

Due to the fact that the length of reflection packets is usually much longer than that of attack packets, attackers can use less network bandwidth to attack the target.

In addition, attackers can also amplify the size of reflected packets by sending a large number of attack requests to the server, further increasing the power of the attack.

This code uses the Shodan API to search for a list of publicly available Memcached servers, and then uses a multi-threaded approach to attack the target IP. The attack parameters include target IP, target port number, number of attack threads, attack duration, and reflection amplification factor.

During the attack, the code will continuously print attack data until the attack ends

Please note that 'YOUR_API_KEY' must be switched to an upgraded version of Shodan's API

# 初始化 Shodan API
api_key = "YOUR_API_KEY"
api = shodan.Shodan(api_key)

运行方法
sudo python3 连毅霖自制memcached伪造反射攻击脚本.py target_ip 这个是您要攻击的网站服务器ip target_port 这个是目标网站服务器的端口号 threads 这个是攻击使用的线程数 duration 这个是攻击持续时间（秒）
注意此代码是我学习python和网络攻防的作业发在这里是提供给大家学习的请不要用于非法用途我不会为你承担任何法律责任


Please note that this code is my homework on learning Python and network attack and defense. It is provided here for everyone to learn. Please do not use it for illegal purposes. I will not assume any legal responsibility for you
