#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyttsx3
import os
pyttsx3.speak("Hello how can i help you")

print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")

print("'''''''''''''''''''''''''''''''''''''''''''''    DHEE BOT    ''''''''''''''''''''''''''''''''''''''''''''''")

print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")

  
while True:
  print("chat with me with ur requirements : " ,end='')
  p = input()

  if (("run" in p) or ("open" in p) or ("launch" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p) or ("text" in p)):
    pyttsx3.speak("Here we go")
    os.system("notepad")
    print()
    print("........................................................................................................")
    print()

  elif (("run" in p) or ("open" in p) or ("launch" in p) or ("execute" in p)) and (("chrome" in p) or ("browser" in p)):
    pyttsx3.speak("Here we go")
    os.system("chrome")
    print()
    print("........................................................................................................")
    print()

  elif (("run" in p) or ("open" in p) or ("launch" in p) or ("execute" in p)) and (("vlc" in p) or ("player" in p) or ("media" in p)):
    pyttsx3.speak("Have fun")
    os.system("vlc")
    print()
    print("........................................................................................................")
    print()

  elif (("run" in p) or ("open" in p) or ("launch" in p) or ("execute" in p)) and (("taskmanager" in p)):
    pyttsx3.speak("Here we go")
    os.system("taskmgr")
    print()
    print("........................................................................................................")
    print()
  

  elif ("exit" in p):
    pyttsx3.speak("Thank you have a great day")
    print()
    print("-----------------------------------------------------  THANK YOU  --------------------------------------")
    break
    

  else:
    pyttsx3.speak("sorry its not available")
    print("--------------------------------------------------------------------------------------------------------")

