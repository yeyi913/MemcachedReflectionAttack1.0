# MemcachedReflectionAttack1.0
该代码实现了一种基于 Memcached 的反射攻击，它利用了 Memcached 服务器的 UDP 协议中的某些漏洞。
攻击者可以伪造源 IP 地址向一个开放的 Memcached 服务器发送一个带有攻击负载的 UDP 数据包，然后服务器将响应数据包发送回伪造的源 IP 地址。
由于反射数据包的长度通常比攻击数据包长得多，因此攻击者可以使用较少的网络带宽来对目标进行攻击。
此外，攻击者还可以通过向服务器发送大量的攻击请求来放大反射数据包的大小，进一步增加攻击的威力。
该代码使用了 Shodan API 搜索公开的 Memcached 服务器列表，然后使用多线程的方式对目标 IP 进行攻击。攻击参数包括目标 IP、目标端口号、攻击线程数、攻击持续时间和反射放大倍数等。
在攻击过程中，代码会不断打印攻击数据，直到攻击结束
