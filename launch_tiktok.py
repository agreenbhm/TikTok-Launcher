from zeroconf import ServiceBrowser, ServiceListener, Zeroconf
import time, sys, os

class MyListener(ServiceListener):

    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Service {name} updated")

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Service {name} removed")

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)
        #print(f"Service {name} added, service info: {info}")
        #sys.stdout.write(str(info.port))
        os.system("/data/data/com.termux/files/usr/bin/adb connect localhost:" + str(info.port))
        os.system("echo " + str(info.port) + " > /data/data/com.termux/files/home/adb_port.txt")
        os.system("/data/data/com.termux/files/usr/bin/adb shell am start --user 10 " + sys.argv[1])
        os.system("/data/data/com.termux/files/usr/bin/adb disconnect")

zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_adb-tls-connect._tcp.local.", listener)
time.sleep(1)
zeroconf.close()

