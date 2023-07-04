# randomProject
Random Project is a multi disciplinary project that generates random numbers.</br>
</br>
It all started in the early 00's, with using the random feature in winamp. I realissed, that it's not so random as it supposed to be. At that point I become interrested in computer genereated random numbers and I went back to this problem every once in a while. Through this interrest I came accross videos expaining computer generated random numbers and videos on building true random number generators. This repository is my take on generating true random numbers.

#### radiationCounter
Also this repository contains the code for the radiation counter project, as the two are closely related. I am considering though to separete the two, as it would make more sense.
To see a chart of the background radiation in my livingroom in Penicuik in the past 12 hours, visit [thingSpeak](https://thingspeak.com/channels/2206987).

## The equipment
The hearth of the project is a [J305 geiger-muller tube and it's associated circuits](/documentation/radiationCounter.JPG). It can detect ionising radiation and send an interrupt an signal when it's detected.</br>
The brains is a [Raspberry Pi model B](/documentation/rasPi1B.JPG). It's responsible for running the code generating random numbers (randomEngine.py), and hosting a website to list the generated numbers. Also as the project grew arms and legs, it counts radiation (radiationCounter.py) and reports them to thinSpeak.com.</br>
The two are connected through a [logic level shifter](/documentation/logicLevelConverter.JPG) to take care of the 5v <===> 3.3v conversion.

## Software
The random numbers are taken care of randomEngine.py</br>
The radiation is counted by radiationCounter.py

---

my dumping ground:<br>
I'll eventually create an organized documentation as I go along

list of resouces:
raspi security tips: https://raspberrytips.com/security-tips-raspberry-pi/</br>
set up git: https://projects.raspberrypi.org/en/projects/getting-started-with-git/</br>
raspi pinout: https://pinout.xyz/pinout/pin7_gpio4</br>
raspi gpio: https://www.makeuseof.com/tag/raspberry-pi-gpio-pins-guide/</br>
https://sourceforge.net/p/raspberry-gpio-python/wiki/browse_pages/</br>
nginx default www folder: https://serverfault.com/questions/718449/default-directory-for-nginx</br>
python wait for edge: https://stackoverflow.com/questions/31303718/python-whats-the-most-efficient-way-to-wait-for-input</br>
and: http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio</br>

Andreas Spiess geiger counter: https://www.youtube.com/watch?v=K28Az3-gV7E&ab_channel=AndreasSpiess
 and: https://github.com/SensorsIot/Geiger-Counter-RadiationD-v1.1-CAJOE-/blob/master/simpletest

publish to thigSpeak: https://uk.mathworks.com/help/thingspeak/use-raspberry-pi-board-that-runs-python-websockets-to-publish-to-a-channel.html




