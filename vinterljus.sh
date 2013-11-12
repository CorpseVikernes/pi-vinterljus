#!/bin/bash

## Vinterljus
PROG= "python"
PROG_PATH = "/usr/bin"
PROG_ARGS = ""
PID_PATH = "/var/run/"


start() {
    if [ -e "$PID_PATH/$PROG.pid" ]; then
        ## Program is running, exit with error.
        echo "Error! $PROG is currently running!" 1>&2
        exit 1
    else
        ## Change from /dev/null to something like /var/log/$PROG if you want to save output.
        $PROG_PATH/$PROG $PROG_ARGS 2>&1 >/dev/null &
        touch "$PID_PATH/$PROG.pid"
	sleep 2 
	echo "-----------------------"
	echo "Starting Camera .. "
	$PROG /home/pi/pi-vinterljus/campy/campy.py &
	sleep 1
	echo "Camera running!"
	echo "-----------------------"
	echo "Starting PIR .."
	$PROG /home/pi/pi-vinterljus/pir/pir.py &
	sleep 1
	echo "PIR running!"
	echo "-----------------------"
	echo "Starting PiAlive .."
	$PROG /home/pi/pi-vinterljus/pialive/pialive.py &
	sleep 1
	echo "PiAlive running!"
	echo "-----------------------"
	echo "Starting PiButton .."
	$PROG1 /home/pi/pi-vinterljus/pibutton/pibutton.py &
	sleep 1
	echo "PiButton running!"
	echo "-----------------------"
	echo "PI-VINTERLJUS INITIATED"
    fi
}


start() {
    sleep 2 
    echo "-----------------------"
    echo "Starting Camera .. "
    $PROG /home/pi/pi-vinterljus/campy/campy.py &
    sleep 1
    echo "Camera running!"
    echo "-----------------------"
    echo "Starting PIR .."
    $PROG /home/pi/pi-vinterljus/pir/pir.py &
    sleep 1
    echo "PIR running!"
    echo "-----------------------"
    echo "Starting PiAlive .."
    $PROG /home/pi/pi-vinterljus/pialive/pialive.py &
    sleep 1
    echo "PiAlive running!"
    echo "-----------------------"
    echo "Starting PiButton .."
    $PROG1 /home/pi/pi-vinterljus/pibutton/pibutton.py &
    sleep 1
    echo "PiButton running!"
    echo "-----------------------"
    echo "PI-VINTERLJUS INITIATED"
}

stop() {    

    if [ -e "$PID_PATH/$PROG.pid" ]; then
        ## Program is running, so stop it
        killall $PROG

        rm "$PID_PATH/$PROG.pid"
        
        echo "$PROG stopped"
    else
        ## Program is not running, exit with error.
        echo "Error! $PROG not started!" 1>&2
        exit 1
    fi
}


## Check to see if we are running as root first.
## Found at http://www.cyberciti.biz/tips/shell-root-user-check-script.html
if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root" 1>&2
    exit 1
fi

case "$1" in
    start)
        start
        exit 0
    ;;
    stop)
        stop
        exit 0
    ;;
    reload|restart|force-reload)
        stop
        start
        exit 0
    ;;
    **)
        echo "Usage: $0 {start|stop|reload}" 1>&2
        exit 1
    ;;
esac