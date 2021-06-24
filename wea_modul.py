import os
import time
import datetime
import enquiries
import json
import copy
import turtle
os.system("clear")

print("""Wea Engine 3.1 - Python""")
while True:
    optionsd = ['yeni proje', 'python konsolu']
    choiced = enquiries.choose(None, optionsd)

    
    if choiced == "yeni proje":
      ad = input("proje adı:")
      try:
        os.chdir("Projeler")
      except:
        os.mkdir("Projeler")
        os.chdir("Projeler")
      os.mkdir(ad)
      os.chdir(ad)
      
      with open(ad + ".json", "w") as bilgiler:
        bilgiler.write('''{
  "ad": "'''+ad+'''",
  "main": "'''+ad+'''"
} ''') 
      break
    if choiced == "python konsolu":
      while True:
          

          x = input(">>> ")
          if x == 'q':
            break

          try:

            y = eval(x)
            if y: print(y)
          except:
              try:
                exec(x)
              except Exception as e:
                print("PythonError:", e)
      break