#! /usr/bin/env pyhton3
from envstatus import EnvStatus
import os
import sys
import time
import datetime


CHECK_SPAN = int(os.environ.get('CHECK_SPAN', '10'))

#　MACアドレスを取得
BLUETOOTH_DEVICEID = os.environ.get('BLUETOOTH_DEVICEID', 0)
BLUETOOTH_DEVICE_ADDRESS = os.environ.get('BLUETOOTH_DEVICE_ADDRESS', None)
if BLUETOOTH_DEVICE_ADDRESS is None:
    sys.exit('No sensors found')

o = EnvStatus(bt=BLUETOOTH_DEVICEID)
uId = o.setRequest(BLUETOOTH_DEVICE_ADDRESS)
o.start()

latest_update = datetime.datetime.now()
while True:

    #環境センサーから取得しているデータ
    data = o.getLatestData(uId)


    if data is not None:

        if data.tick_last_update > latest_update:
            print('Illumination: {} lx'.format(data.val_light))
            # センサーデータの確認
            #print('センサーデータ：　{} '.vars(data))
            print('Sensor Data: {}'.format(data.vars()))

        latest_update = data.tick_last_update

    time.sleep(CHECK_SPAN)
