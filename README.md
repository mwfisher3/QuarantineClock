# QuarantineClock

Welcome to Quarentine Clock

Add the following to "/etc/xdg/lxsession/LXDE-pi/autostart"

@lxterminal -e /home/pi/QuarantineClock/BackLight.py
@chromium-browser --incognito  --noerrdialogs --disable-desktop-notifications -update-kiosk --check-for-update-interval=1 --simulate-critical-update /home/pi/QuarantineClock/today.html


