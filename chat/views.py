import time
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
def job():
 import time
 start_time = time.time()
 driver = webdriver.Chrome() 
 driver.get("https://www.nseindia.com/option-chain")
 time.sleep(1)
 data = driver.find_elements(By.XPATH,('//*[@id="equity_optionChainTable"]'))
 arr1 = data[0].text.split("\n")
 nify_options = []
 for i in arr1[22:-1]:
  nify_options.append(i.split(" "))
 for i in nify_options:
  print(i)
 driver.close()
 print("My program took", time.time() - start_time, "to run")

def cop(request):
 channel_layer = get_channel_layer()
 async_to_sync(channel_layer.group_send)(
  'nifty',
  {
   'type':'websocket.send',
    'text':'hi from auto'
  }
 )
 print("done\n\n\n\n\n")
 return HttpResponse("okay")