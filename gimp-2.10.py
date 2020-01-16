# GIMP-2.10.10を起動し、スクリーンショットを取得するためのJythonのスクリプト。
# SikuliX-2.0.1でのみテストを行っています。
# URL: https://pandanote.info/?p=3338
# Script to invoke GIMP-2.10.10 and to take a screenshot by it on SikuliX environment.
# This script is tested with SikuliX-2.0.1.
click("1542506859041.png")
wait(2)
click("1542509349902.png")
wait(13)
click(Pattern("1542510352713.png").targetOffset(-232,14))
wait(1)
click("1542510443808.png")
wait(1)
click("1542510526572.png")
wait(1)
click(Pattern("1579143851992.png").targetOffset(-29,-3))
wait(1)
click(Pattern("1579143983163.png").targetOffset(10,10))
type(Key.BACKSPACE)
type('10')
click(Pattern("1542510757822.png").similar(0.37).targetOffset(1,52))
