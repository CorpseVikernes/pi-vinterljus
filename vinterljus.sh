#! /bin/bash

sleep(2)
echo "-----------------------"
echo "Starting Camera .. "
sudo python /home/pi/pi-vinterljus/campy/campy.py &
sleep(1)
echo "Camera running!"
echo "-----------------------"
echo "Starting PIR .."
sudo python /home/pi/pi-vinterljus/pir/pir.py &
sleep(1)
echo "PIR running!"
echo "-----------------------"
echo "Starting PiAlive .."
sudo python /home/pi/pi-vinterljus/pialive/pialive.py &
sleep(1)
echo "PiAlive running!"
echo "-----------------------"
echo "Starting PiButton .."
sudo python /home/pi/pi-vinterljus/pibutton/pibutton.py &
sleep(1)
echo "PiButton running!"
echo "-----------------------"
echo "PI-VINTERLJUS INITIATED"