MeltTech is a Fork Nemesis PI / picoThermal which is a fork off of picoReflow by [apollo-ng]. It is intended to make it more 
versatile (suited for ceramic Pottery kilns) by adding several features:
Some Functions below are work in progress see config.py

Not Limited by stages and or programs ,you can have Thousands depending on PI4 models memory 4Gb or 8Gb
* Automatic PID tuning
* Time and temperature units defined per profile
* Added a High Limit Emergency shut off     Heating will be turned off and program stopped
* Added a Thermocouple Offset     adjust if needed to calibrate
* Removed CSV Logging MAKES IT SAFE NOT WRITING TO THE DISK! ACCESS LOGGING DATA IN TERMINAL CONTROLLER IS RUNNING IN only in manual mode or graph screen shot       will move to cloud. 
* Use the Live graph to help diagnose loose thermocouple connections and kiln issues such as relays and element wear over time. 
* added 2 key press Stop Button option also setting up 2 and 3 zone removed simulate function still on single zone
* added Talking Kiln Controller update and bungs in terminal notification! currently no talking implemented.still in code though.

This software Perfect for controlling a electric kiln and is works reliably with full remote control if needed via Phone ,Tablet or PC etc.. 
The added options make it suitable for a much wider range of thermal control.

* added Hot Links to make getting Help and Firing Profiles for your Nemesis PI controller easier and added multi configs for easy copy and paste for Heat Treatment kilns as they do long holds at many different temperatures easy as copying and pasting config then restart controller to take effect quicker than having to constantly auto tuning kilns like simple PID controllers takes just 1 minute instead of some times hours like older controllers

* Removed talking from controller make more user friendly talking has been hashed out can be unhashed but directory pointing needs to be specific with pygame.
so we decide to remove it at present until the problem is rectified pygame seems to also now casuing problems on install

* Disabled Logging safer to not log if disk read/write error occurs or system becomes read only
.
* Has error codes and will stop on errors for "safety" for max 31855k current driver supported module more coming soon very soon type k , n , r ,s ,j ,t, etc
NO connection     Thermocouple sensor break

* Error Fault code 4 = Temperature reading 4 deg C means line fault or thermocouple board issue

Just keep your controller software updated ,come back from time to time to see the advancements we are making!!!

Use "simplescreenrecorder" from the app store in Linux to record your firing logs or if in manual mode copy and paste out of Terminal into speadsheet and save
Rememeber share and email your friends your working firing programs great to help out the Noobs

Great for Glass kilns pottery kilns
Downloadable Firing Profiles Matching orton cone chart easily added to your controller download only the ones need to keep the list short see MeltTech Website

Watch this Space!!!

Special thanks for the auto tune function implementation it just works!!!
cheers to 
Peter Thompson
Petronator
Also Special Thanks To JBruce12000 for all his hard work in many other areas of the programming making it a way better controller
mburazin Marko Burazin for the scheduled starting sequence

Updates will be maintained for free by us and the community make it your own expand it!
Please send us a message to help make it better!

Step 1)
INSTALL KILN CONTROLLER
Copy lines below one by one and paste in terminal press ,answer Y to any prompts and press Enter.

$ git clone https://github.com/MeltTechAu/MeltTech.git                      
$ sudo pip install ez-setup                               
$ sudo apt install libffi-dev                          
$ sudo pip3 install greenlet bottle gevent gevent-websocket                         
$ sudo apt-get install python3-pip python3-dev libevent-dev git -y                         
$ sudo su                       
$ update-alternatives --install /usr/bin/python python /usr/bin/python3 1                       

Thats it now you can start the controller Manual Load Mode see full manual other options SUCH AS REMOTE VIEWING using VNC

Step 2)
Manual Server Startup
Copy lines below and paste in terminal press enter or click on icon MT icon in Open in notepad edit where it says "pi" replace with your computer name and save and copy to desktop then you can double click icon instead of using terminal

cd MeltTech
python picoreflowd.py

Then open web browser on the 
MeltTech and enter into address bar 127.0.0.1:8081 Press enter ,controller interface will load.refresh browser if not loaded correctly and not seeing a graph or programs

Step 3)
Once Autotuned then set up below and it will load in the back ground just open web browser
Autostart Server on Boot(do this after Auto Tuning your MeltTech
If you want the server to autostart on boot, run the following commands

sudo nano /etc/rc.local

add the line:

`sudo python /home/pi/NemesisPI/picoreflowd.py &`

Add above line just above last exit at bottom of file once changed hold down Ctrl key + o to save then press enter then close terminal close Terminal and reboot Nemesis PI.

Step 4)Auto Tuning see videos and full manual on install page at melttech.com.au

For more updated help see MeltTech help page as things change in the operating system from time to time we 
update as fast as we can to make sure all is working

This quick install file can be found on our install page and manual page see full manual/Videos for AutoTuning
HAVE GOOD WIFI AND IF IT DOSN'T WORK REDO ABOVE BUT IT WILL

License
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.

picoReflow
For more info on the parent project, see picoReflow: https://apollo.open-resource.org/mission:resources:picoreflow

MeltTech 2022






