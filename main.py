from pynput.keyboard import Controller, Key
import time

keyboard = Controller()


arg = str(input('The Word/Sentence: '))

wordlist = []

times = int(input('Amount of fire: '))

confirmation = str(input('Confirmation(Y/N): ')).lower()

speed = float(input('Speed of Spam(in seconds): '))


if confirmation == 'y':
  countdown = 10

  print('ETA 10 seconds.')
  
  
  for _ in range(11):
    print(countdown)
    countdown -= 1
    time.sleep(1)


  for letter in arg:
    wordlist.append(letter)


   
  for _ in range(times-1):
    for key in wordlist:
      keyboard.press(key)
      keyboard.release(key)
      
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(speed)
  print('Task Completed.') 
else:
  print('Okay, exiting!')
