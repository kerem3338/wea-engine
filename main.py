import os
import sys
import json
import enquiries


with open("ilk.txt", "r+") as ilk:
  if ilk.read() == "ilk":
    print("""WEA Engine 3.1
WEA Engine © 2021 Dios yazılım

Merhaba ben Wbot size wea'yı anlatmak için buradayım.
Wea oyun motoru 3.1 sürümünü indridiğiniz için teşekkürler, wea basit oyunlar oluşturmanıza imkan sunar ayrıca python programlama """)
  ilk.write("_pas")
print("""           Wea Engine 3.1
-----------------------------------------
    python / js / weascript
    """)
while True:
    options = ['proje aç', 'yeni proje', 'yardım', 'ayarlar']
    choice = enquiries.choose(None, options)
    if choice =="ayarlar":
      print("Bakımda xD")
    
    if choice == "yeni proje":
      seçim = ['python', 'html']
      seçenek = enquiries.choose(None, seçim)

    
      if seçenek == "python":
        import wea_modul
        break

      
  
