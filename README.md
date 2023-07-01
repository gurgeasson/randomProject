# randomProject
Random Project is a multi disciplinary project that generates random numbers.

It started with using the random feature in winamp and realising, that it's not so random as it supposed to be. Ever since I went back to this problem every once in a while, came accross videos expaining computer generaetd random numbers or building true random number generators. This repository is my take on generating true random numbers.

The hearth of the project is a J305 geiger-muller tube and it's associated circuits. It can detect ionising radiation and send an interrupt an signal when it's detected.
The brains is a Raspberry Pi model B. It's responsible for running the code generating random numbers (randomEngine.py), and hosting a website to list the generated numbers. Also as the project grew arms and legs, it counts radiation (radiationCounter.py) and reports them to thinSpeak.com.




I'll eventually create an organized documentation as I go along

---

here is my dumping ground:<br>
quick notes:

list of resouces:
raspi security tips: https://raspberrytips.com/security-tips-raspberry-pi/</br>
set up git: https://projects.raspberrypi.org/en/projects/getting-started-with-git/</br>
raspi pinout: https://pinout.xyz/pinout/pin7_gpio4</br>
raspi gpio: https://www.makeuseof.com/tag/raspberry-pi-gpio-pins-guide/</br>
https://sourceforge.net/p/raspberry-gpio-python/wiki/browse_pages/</br>
nginx default www folder: https://serverfault.com/questions/718449/default-directory-for-nginx</br>
python wait for edge: https://stackoverflow.com/questions/31303718/python-whats-the-most-efficient-way-to-wait-for-input</br>
- and: http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio</br>

Andreas Spiess geiger counter: https://www.youtube.com/watch?v=K28Az3-gV7E&ab_channel=AndreasSpiess
 and: https://github.com/SensorsIot/Geiger-Counter-RadiationD-v1.1-CAJOE-/blob/master/simpletest



publish to thigSpeak: https://uk.mathworks.com/help/thingspeak/use-raspberry-pi-board-that-runs-python-websockets-to-publish-to-a-channel.html




