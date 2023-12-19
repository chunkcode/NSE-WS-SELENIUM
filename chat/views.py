import time
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync



 

def job1():
 driver = webdriver.Chrome() 
 driver.get("https://www.nseindia.com/option-chain")
 try:
  channel_layer = get_channel_layer()
  time.sleep(1)
  data = driver.find_elements(By.XPATH,('//*[@id="equity_optionChainTable"]'))
  arr1 = data[0].text.split("\n")
  nify_options = []
  for i in arr1[22:-1]:
   nify_options.append(i.split(" "))
  async_to_sync(channel_layer.group_send)(
            'test',
            {
                'type':'chat_message',
                'message':nify_options
            }
        )
 except:
  pass

def job2():
 driver = webdriver.Chrome() 
 driver.get("https://www.nseindia.com/market-data/live-equity-market")
 try:
  channel_layer = get_channel_layer()
  time.sleep(1)
  data = driver.find_elements(By.XPATH,('//*[@id="tableLiveMarket-equity-stock"]'))
  arr2 = data[0].text.split("\n")[20:]
  i = 0
  values = []
  while i < len(arr2):
    if len(arr2[i].split(" ")) > 12:
        values.append(arr2[i].split(" "))
        i = i+1
    else:
        values.append(arr2[i].split(" ")+arr2[i+1].split(" "))
        i = i+2
  async_to_sync(channel_layer.group_send)(
            'test',
            {
                'type':'chat_message2',
                'message':values
            }
        )
 except:
  pass
 

def cop(request):
 channel_layer = get_channel_layer()
 async_to_sync(channel_layer.group_send)(
            'test',
            {
                'type':'chat_message',
                'message':'from views'
            }
        )
 print("done\n\n\n\n\n")
 return HttpResponse("okay")