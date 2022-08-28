import time
import os
import ppadb
from ppadb.client import Client as AdbClient
from xml.dom import minidom


def connect():
    client = AdbClient(host='127.0.0.1', port=5037)
    return client



if __name__ == '__main__':
    client = connect()
    devices = client.devices()
    if len(devices) == 0:
        print('No devices')
        quit()


    def power(device):
        device.shell('input keyevent 26')


    def deblock(device):
        device.shell('input keyevent 82')


    def always_enable(device):
        device.shell('svc power stayon true')


    def dump(device):
        device.shell('uiautomator dump /sdcard/view3.xml')

    def push(device):
        device.pull ('/sdcard/view3.xml')


    def text_finder():
        global l
        global a
        xmldoc = minidom.parse('view3.xml')
        product_list = xmldoc.getElementsByTagName('node')
        print("No of Items : ", len(product_list, ))

        for product in product_list:
            a = (product.attributes['text'].value)
            k = (product.attributes['bounds'].value)
            c = ''
            if a != c:
                n = k.replace('[', "")
                m = n.replace(']', " ")
                y = m.replace(',', ' ')
                l = 'input tap ' + y

        return l


    for device in devices:
        print(f'Connected to {device}')
        dump(device)




