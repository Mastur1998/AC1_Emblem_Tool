I'm writing this assuming you know nothing about python

Step 1: Downloading python
Go to python.org and download the intaller, when installing, mark the "add to path" checkbox
and then 'install now'

Step 2: Dowloading python packages
Open your cmd window (press windows+r, then type 'cmd' into the small window that appears),
then type the following commands to intall the necessary packages:
-pip install numpy
-pip install opencv-python
-pip install pynput
-pip install pywin32
(I guess i should mention i have no idea if this will work on  Linux/Mac)
Typing 'pip list' after this is done should show all packages and their versions
You can do google search to find what each ackage does.

Step 3: Create your emblem
I'd recommend usign paint.net for this because its free and it does what its suposed to do
the image has to be a png, 64x64 pixels in size, and the color palette has to be of at most
16 unique colors, one of them being the 'transparent' color (alpha value of zero).
When saving this image, make sure to place it next to the python file.

Step 4: Set up your emulator
The script assumes you're using duckstation's default keyboard mappings, that is,
d-pad mapped to wasd, the face buttons to ijkl, and the left/right front triggers to 1 and 3.
Boot up the game, go to your garage and open the emblem editor.
Press 1 (left trigger) to leave the paint selection on the transparent color.
Press l (circle) to open the menu, set the zoom to x4, the menu should close itself.
Open the menu again and choose clear, the menu should close and the canvas should be blank.
Leave the emulator there

Step 5: Edit two lines
On your search bar type 'IDLE' and open the python app.
Press ctrl+o, find the autopilot script and open it.
On line 8, change the emulator name to the name your emulator has when hovering over it on the taskbar
On line 9, change the source name to the filename of the emblem you just made
Both of these names are caps sensitive, as an alternative you can just put the emulator at the forefront
manually after starting the script, and set 'Emblem.png' as the emblem filename

Step 6: Run it!
While youre still with the script open, press f5, the python shell will pull up, after 5 seconds the emulator 
will pull up (5 seconds is enough to pull up the emulator manually).
If you positioned your windows strategically, you should now be able to see both the emulator and the 
IDLE shell side by side, from now on you should NOT touch anything, otherwise the scrip will desync and
everything will go to ruin.
If you notice one of the lines wasn't drawn correctly, memorize or write down (not on your computer) the
line number, the script should still draw the next lines properly.
If you notice one of the lines is not being drawn at the rigth height, you may be able to press 'w' or 's'
to move the pointer to the right height.
If you notice the color selector is not using the rigth color, you may be able to press '1' or '3' to
move the color selector to the rigth color.
Once the script is done (or interrupted ny closing the IDLE shell), you can then run it again with various
settings to fix mistakes by pressign shift+f5.
Typing 'Palette' will only input the color palette of the image without messing with the emblem,
likewise, typing 'Emblem' instead will only draw without re-doing the palette.
You can instead type 'UpLeft', 'UpRight', 'DownLeft' or 'DownRight' to re-draw a specific quadrant of
the emblem, if you want to re-draw starting from a specific line, type the quadrant and the numer line,
if you want to re-draw starting and ending on a specific line, type the quadrant and two numbers.
For example lets say line 6 and 7 on the bottom left had mistakes, i would type 'DownLeft 6 8', and the
script would re-draw those and only those two lines.
Keep in mind, every time you restart the script you have to place the color selector on the transparent
color, the pen tool selected, the cursor ready to draw, and the zoom at x4.

Step 7: Feedback
I honestly don't expect the script to need any reworks, major fixes or changes, but if anyone wants to reach
me with suggestions, complaints or just wanna share their emblem, my reddit username is u/DonMastur, or 
alternatively post at r/armoredcore
