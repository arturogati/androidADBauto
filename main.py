import time
import os
from ppadb.client import Client as AdbClient
from xml.dom import minidom


def connect():
    client = AdbClient(host='127.0.0.1', port=5037)
    return client   #device

if __name__ == '__main__':
    client = connect()
    devices = client.devices()
    if len(devices) == 0:
        print('No devices')
        quit()




    def delete_android(device):
        device.shell("rm /sdcard/view.xml")

    def delete_comp():
        path = ''
        os.remove(path)

    def call_in(device):
        device.shell('input keyevent 5')

    def call_end(device):
        device.shell('input keyevent 6 ')

    def settings(device):
        device.shell('input keyevent 210')

    def power(device):
        device.shell ('input keyevent 26')

    def home(device):
        device.shell ('input keyevent 3')

    def swipe(device):
        device.shell('input swipe 200 500 200 0')

    def deblock(device):
        device.shell ('input keyevent 82')

    def letter(device):
        device.shell('input text "VoLTE calls SIM 1"')

    def finder(device):
        device.shell ('am start -n com.samsung.android.app.galaxyfinder')

    def dump(device):
        device.shell('uiautomator dump /sdcard/view3.xml')

    def always_enable(device):
        device.shell ('svc power stayon true')

    def push(device):
        device.pull('/sdcard/view3.xml')


    def text(device):
        r = 'adb shell input text ""'
        device.shell(r)


    def xml_volte1():
        global l
        xmldoc = minidom.parse('view.xml')
        product_list = xmldoc.getElementsByTagName('node')
        print("No of Items : ", len(product_list, ))

        for product in product_list:
            a = (product.attributes['text'].value)
            k = (product.attributes['bounds'].value)
            c = 'VoLTE calls SIM 1'
            if a == c:
                n = k.replace('[', "")
                m = n.replace(']', " ")
                y = m.replace(',', ' ')
                l = 'input tap ' + y

        return l
    def xml_volte2():
        global l
        xmldoc = minidom.parse('view3.xml')
        product_list = xmldoc.getElementsByTagName('node')
        print("No of Items : ", len(product_list, ))

        for product in product_list:
            a = (product.attributes['text'].value)
            k = (product.attributes['bounds'].value)
            c = 'VoLTE calls SIM 1'
            if a == c:
                n = k.replace('[', "")
                m = n.replace(']', " ")
                y = m.replace(',', ' ')
                l = 'input tap ' + y

        return l


    def xml_search():
        global l
        xmldoc = minidom.parse('view3.xml')
        product_list = xmldoc.getElementsByTagName('node')
        print("No of Items : ", len(product_list, ))

        for product in product_list:
            a = (product.attributes['text'].value)
            k = (product.attributes['bounds'].value)
            c = 'Search'
            if a == c:
                n = k.replace('[', "")
                m = n.replace(']', " ")
                y = m.replace(',', ' ')
                l = 'input tap ' + y

        return l


    def volte_on(device):
        power(device)
        deblock(device)
        time.sleep(5)
        swipe(device)
        always_enable(device)
        dump(device)
        time.sleep(4)
        push(device)
        time.sleep(4)
        xml_search()
        time.sleep(5)
        device.shell(l)
        time.sleep(7)
        letter(device)
        time.sleep(4)
        delete_android(device)
        delete_comp()
        time.sleep(5)
        dump(device)
        push(device)
        time.sleep(3)
        xml_volte1()
        device.shell(l)
        time.sleep(3)
        delete_android(device)
        delete_comp()
        time.sleep(5)
        dump(device)
        push(device)
        time.sleep(3)
        xml_volte1()
        device.shell(l)
        time.sleep(3)
        delete_android(device)
        delete_comp()







    for device in devices:
        print(f'Connected to {device}')
        dump(device)

















