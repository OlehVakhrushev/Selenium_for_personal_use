from time import sleep

import speech_recognition as sr
import os
import sys
import pyttsx3
import webbrowser

from selenium import webdriver
from selenium.webdriver import ActionChains


def talk(words):
 print(words)
 engine = pyttsx3.init()
 engine.say(words)
 engine.runAndWait()


talk("Hello, ask my something")


def command():
 r = sr.Recognizer()


 with sr.Microphone() as source:
  print("Talk")
  r.pause_threshold = 1
  r.adjust_for_ambient_noise(source, duration=1)
  audio = r.listen(source)

  try:
   zadanie = r.recognize_google(audio).lower()
   print("You said: " + zadanie)
  except sr.UnknownValueError:
   talk("I don't understand")
   zadanie = command()
  return zadanie

def makeSomething(zadanie):
 if 'open website' in zadanie:
  talk("I open")
  url = 'https://www.google.ru/'
  webbrowser.open(url)
 if 'invite friends' in zadanie:
  driver = webdriver.Chrome("C:\\Users\\Oleg\\PycharmProjects\\Selenium_Ellie\\Tests\\chromedriver\\chromedriver_win32\\chromedriver.exe")
  driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
  driver.maximize_window()
  #        driver.find_element_by_xpath("(//data-tracking-will-navigate[text()='Sign in'])[0]").click()
  driver.find_element_by_id('username').send_keys("akradabaska@gmail.com")
  driver.find_element_by_id('password').send_keys("Z4055966z")
  driver.find_element_by_xpath("(//button[text()='Sign in'])").click()
  sleep(2)
  driver.find_element_by_id("mynetwork-tab-icon").click()
  sleep(4)
  element = driver.find_element_by_xpath("//span[text()='Connect']")

  actions = ActionChains(driver)
  actions.move_to_element(element).perform()
  for i in range(0, 15):
   for i in range(0, 4):
    driver.find_elements_by_xpath("//span[text()='Connect']")[i].click()
   driver.find_element_by_id("mynetwork-tab-icon").click()
   sleep(4)
   element = driver.find_element_by_xpath("//span[text()='Connect']")

   actions = ActionChains(driver)
   actions.move_to_element(element).perform()

  driver.quit()

 if 'open movies' in zadanie:
  talk("Let's go to the movies")
  url = 'http://fanserial.net/'
  webbrowser.open(url)

 if 'youtube music' in zadanie:
   talk("I'm down for it")
   url = 'https://www.youtube.com/watch?v=NL8G5-CLQ5E'
   webbrowser.open(url)

 if 'open youtube' in zadanie:
   talk("One moment")
   url = 'https://www.youtube.com/'
   webbrowser.open(url)
 elif 'stop' in zadanie:
  talk("Yes of course, no problem")
  sys.exit()


while True:
 makeSomething(command())







