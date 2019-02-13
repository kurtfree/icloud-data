#!/usr/bin/env python3
import sys
import os
from pyicloud import PyiCloudService

# https://github.com/picklepete/pyicloud

username = sys.argv[1]
password = sys.argv[2]

api = PyiCloudService(username, password)

output = open("output.txt", "w")
try:
    devices = api.devices # {'xxxxXQtf3tUrd/jlD86ELtMmc8627Qtr+jktuxxxxexDJ0yzc58ivuxxxxxxxxxx': <AppleDevice(iPad: iPad (2))>}
    output.write(str(devices))
except:
    print ("ERROR getting devices")
try:
    location = api.iphone.location() # {'isOld': False, 'isInaccurate': False, 'altitude': 0.0, 'positionType': 'Wifi', 'latitude': xx.yyyyyyyyyyyyyy, 'floorLevel': 0, 'horizontalAccuracy': 65.0, 'locationType': '', 'timeStamp': 1550071439029, 'locationFinished': False, 'verticalAccuracy': 0.0, 'longitude': xx.yyyyyyyyyyyyyy}
    output.write(str(location))
except:
    print ("ERROR getting location")
try:
    status = api.iphone.status() # {'batteryLevel': 0.8999999761581421, 'deviceDisplayName': 'iPad', 'deviceStatus': '201', 'name': 'iPad (2)'}
    output.write(str(status))
except:
    print ("ERROR getting status")
try:
    content = api.iphone.content #{'msg': None, 'canWipeAfterLock': True, 'baUUID': '', 'wipeInProgress': False, 'lostModeEnabled': False, 'activationLocked': True, 'passcodeLength': 6, 'deviceStatus': '200', 'deviceColor': '1-1-0', 'features': {'MSG': True, 'LOC': True, 'LLC': False, 'CLK': False, 'TEU': True, 'LMG': False, 'SND': True, 'CLT': False, 'LKL': False, 'SVP': False, 'LST': True, 'LKM': False, 'WMG': True, 'SPN': False, 'XRM': False, 'PIN': False, 'LCK': True, 'REM': False, 'MCS': False, 'CWP': False, 'KEY': True, 'KPD': True, 'WIP': True}, 'lowPowerMode': False, 'rawDeviceModel': 'iPad6,11', 'id': 'xxxxXQtf3tUrd/jlD86ELtMmc8627Qtr+jktuxxxxexDJ0yzc58ivuxxxxxxxxxx', 'remoteLock': None, 'isLocating': True, 'modelDisplayName': 'iPad', 'lostTimestamp': '', 'batteryLevel': 0.8899999856948853, 'mesg': None, 'locationEnabled': True, 'lockedTimestamp': None, 'locFoundEnabled': False, 'snd': None, 'fmlyShare': False, 'lostDevice': None, 'lostModeCapable': True, 'wipedTimestamp': None, 'deviceDisplayName': 'iPad', 'prsId': None, 'audioChannels': [], 'locationCapable': True, 'batteryStatus': 'NotCharging', 'trackingInfo': None, 'name': 'iPad (2)', 'isMac': False, 'thisDevice': False, 'deviceClass': 'iPad', 'location': {'isOld': False, 'isInaccurate': False, 'altitude': 0.0, 'positionType': 'Wifi', 'latitude': xx.yyyyyyyyyyyyyy, 'floorLevel': 0, 'horizontalAccuracy': 65.0, 'locationType': '', 'timeStamp': 1550071565711, 'locationFinished': False, 'verticalAccuracy': 0.0, 'longitude': xx.yyyyyyyyyyyyyy}, 'deviceModel': 'EighthGen-1-1-0', 'maxMsgChar': 160, 'darkWake': False, 'remoteWipe': None}
    output.write(str(content))
except:
    print ("ERROR getting content")
try:
    manager = api.iphone.manager # List like devices above with "managers" if the account is managed
    output.write(str(manager))
except:
    print ("ERROR getting manager")
try:
    params = api.iphone.params # {'clientBuildNumber': '11A11', 'clientId': '1A111A11-1AA1-11A1-1AA1-A11A11AA11AA', 'dsid': '11111111111'}
    output.write(str(params))
except:
    print ("ERROR getting params")
try:
    session = api.iphone.session # <pyicloud.base.PyiCloudSession object at 0x104f3d198> (?)
    output.write(str(session))
except:
    print ("ERROR getting session")
try:
    calendar = api.calendar.events() # []
    output.write(str(calendar))
except:
    print ("ERROR getting calendar")
try:
    for c in api.contacts.all():
        contact += c.get('firstName'), c.get('phones')
    output.write(str(contact))
except:
    print ("ERROR getting contacts")
try:
    files = api.files.dir() # ['.do-not-delete']
    output.write(str(files))
except:
    print ("ERROR getting files")
try:
    photos = api.photos.all # Unhandled exception -> socket.gaierror: [Errno 8] nodename nor servname provided, or not known
    output.write(str(photos))
except:
    print ("ERROR getting photos")

output.close()
