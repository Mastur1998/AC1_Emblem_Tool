import sys
import numpy as np
import cv2
from pynput.keyboard import Controller as ctr
from time import sleep
import win32com.client

emulator_name = 'Armored Core (USA)'
source = 'Emblem.png'

def InputKey(key, seconds):
  ctr().press(key); sleep(seconds); ctr().release(key); sleep(0.05)

def InputColorPalette(color_palette):
##Input the palette
  print('Setting up color palette')
  InputKey('3',0.05)
  for color in color_palette:
    InputKey('j',0.05)
    InputKey('w',0.05)
    for value in color:
      InputKey('a',2)
      for i in range(value):
        InputKey('d',0.04)
      InputKey('w',0.05)   
    InputKey('k',0.05)
    InputKey('3',0.05)
  print('Color palette set up')
  sleep(2)

def InputEmblem(color_map, down, right, start=0, end=32): 
##Drawing the emblem
##Moving to selected quadrant
  if not down and not right:
    print('Moving to Upper Left quadrant')
    InputKey('a',2.2)
    InputKey('w',0.7)
  if down and not right:
    print('Moving to Lower Left quadrant')
    InputKey('a',2.2)
    InputKey('s',0.7)
  if not down and right:
    print('Moving to Upper Right quadrant')
    InputKey('d',2.2)
    InputKey('w',0.7)
  if down and right:
    print('Moving to Lower right quadrant')
    InputKey('d',2.2)
    InputKey('s',0.7)
  InputKey('k',1)
##Moving pointer to the corner of the drawing area
  print('Preparing to draw')
  InputKey('a',0.7)
  InputKey('w',0.7)
  InputKey('d', 0.05)
  InputKey('s', 0.05)
  InputKey('a', 0.25)
  InputKey('d', 0.05)
  InputKey('w', 0.25)
  InputKey('s', 0.05)
  for i in range(0,start): InputKey('s',0.05)
  if (start % 2) != 0:
    InputKey('d',2.2)
    InputKey('a',0.05)
##Drawing the selected quadrant
  print('Drawing current quadrant')
  index = 0
  for i in range(start,end):
    if down: i += 32
    i_pair = (i % 2) == 0
    print('Drawing line ' + str(i))
    for j in range(0,32):
      if i_pair: target = color_map[i][j+32 if right else j]
      else: target = color_map[i][63-j if right else 31-j]
      right_dist = target - index
      if right_dist < 0: right_dist += 16
      left_dist = index - target
      if left_dist < 0: left_dist += 16
      if right_dist < left_dist:
        while index != target:
          InputKey('3', 0.05)
          index += 1
          if index > 15: index = 0
      else:
        while index != target:
          InputKey('1', 0.05)
          index -= 1
          if index < 0: index = 15
      InputKey('k', 0.05)
      InputKey('d' if i_pair else 'a', 0.05)
    InputKey('d' if i_pair else 'a', 0.1)
    InputKey('a' if i_pair else 'd', 0.05)
    InputKey('s', 0.05)
  while index != 0:
    InputKey('1', 0.05)
    index -= 1
  print('Done drawing current quadrant')
  

def main():
##Put the emulator at the front
  print('Pulling emulator to the front')
  print('Or maybe you\'re pulling it yourself?')
  shell = win32com.client.Dispatch("WScript.Shell")
  shell.AppActivate(emulator_name)
  sleep(5)

##Open image to be drawn
  print('Opening image')
  img = cv2.imread(source, cv2.IMREAD_UNCHANGED)

##Create color palette and color map from image
  print('Creating color palette and color map')
  color_palette = np.zeros((15,3), dtype=np.int8)
  color_count = 0
  color_map = np.zeros((64,64), dtype=np.int8)
  for i in range(64):
    for j in range(64):
      value = np.floor(img[i][j]/8)
      if value[3] == 0: continue
      found = False
      for index in range(0,color_count):
        if all(value[0:3] == color_palette[index]):
          found = True
          color_map[i][j] = index+1
          break
      if not found:
        color_palette[color_count] = value[0:3]
        color_count += 1
        color_map[i][j] = color_count
        if color_count > 15: print('Image has too many colors')
  print('Color palette and color map done')
  
##Set up the color palette
  if len(sys.argv) == 1 or sys.argv[1] == 'Palette':
    InputColorPalette(color_palette)

##Draw the emblem
  if len(sys.argv) == 1 or sys.argv[1] == 'Emblem':
    InputEmblem(color_map, False, False)
    InputEmblem(color_map, False, True)
    InputEmblem(color_map, True, False)
    InputEmblem(color_map, True, True)
  elif len(sys.argv) == 2:
    if sys.argv[1] == 'UpLeft': InputEmblem(color_map, False, False)
    elif sys.argv[1] == 'UpRight': InputEmblem(color_map, False, True)
    elif sys.argv[1] == 'DownLeft': InputEmblem(color_map, True, False)
    elif sys.argv[1] == 'DownRight': InputEmblem(color_map, True, True)
    else: print('Choose UpLeft, UpRight, DownLeft or DownRight')
  elif len(sys.argv) == 3:
    if sys.argv[1] == 'UpLeft': InputEmblem(color_map, False, False, int(sys.argv[2]))
    elif sys.argv[1] == 'UpRight': InputEmblem(color_map, False, True, int(sys.argv[2]))
    elif sys.argv[1] == 'DownLeft': InputEmblem(color_map, True, False, int(sys.argv[2]))
    elif sys.argv[1] == 'DownRight': InputEmblem(color_map, True, True, int(sys.argv[2]))
    else: print('Choose UpLeft, UpRight, DownLeft or DownRight, and a line to start')
  elif len(sys.argv) == 4:
    if sys.argv[1] == 'UpLeft': InputEmblem(color_map, False, False, int(sys.argv[2]), int(sys.argv[3]))
    elif sys.argv[1] == 'UpRight': InputEmblem(color_map, False, True, int(sys.argv[2]), int(sys.argv[3]))
    elif sys.argv[1] == 'DownLeft': InputEmblem(color_map, True, False, int(sys.argv[2]), int(sys.argv[3]))
    elif sys.argv[1] == 'DownRight': InputEmblem(color_map, True, True, int(sys.argv[2]), int(sys.argv[3]))
    else: print('Choose UpLeft, UpRight, DownLeft or DownRight, and a line to start and end (non-inclusive)')
  
  print('End of program')
    
main()
