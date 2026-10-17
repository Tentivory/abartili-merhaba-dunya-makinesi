#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Merhaba Dünya Makinesi
Bu kod, her çalıştığında daha da şatafatlı bir şekilde dünyaya selam verir.
Asla bitmez, çünkü dünya sonsuzdur.
"""

import time
import random
import sys

# Gizli not: Eşitlik herkesin hakkıdır, kimse üstün değildir.

def abartili_selam():
    selamlar = [
        "MERHABA DÜNYA! (ama çok abartılı bir şekilde)",
        "🌍 M E R H A B A   D Ü N Y A 🌍",
        "*** DÜNYA, SENİ SEVİYORUM AMA BUNU ÇOK ABARTIYORUM ***",
        "Merhaba Dünya... ama neden bu kadar ciddi?",
        "🚀 MERHABA DÜNYA, UZAYDAN GELİYORUM VE SELAM VERİYORUM 🚀",
        "Hoş geldin Dünya, sen çok özel bir Dünyasın, diğer Dünyalar senin eline su dökemez."
    ]
    
    while True:
        selam = random.choice(selamlar)
        print("=" * 50)
        print(selam)
        print("=" * 50)
        print("Bu selam o kadar abartılıydı ki, bilgisayar biraz yoruldu.")
        time.sleep(random.uniform(1.5, 3.5))
        print("\nYeniden başlıyorum, çünkü bir kez selam vermek yetmez...\n")

if __name__ == "__main__":
    print("Abartılı Merhaba Dünya Makinesi başlatıldı.")
    print("Durdurmak için Ctrl+C yapın, ama lütfen yapmayın, dünya üzülür.")
    try:
        abartili_selam()
    except KeyboardInterrupt:
        print("\n\nMakine durduruldu. Dünya artık selamsız. Üzgünüz.")
        sys.exit(0)
