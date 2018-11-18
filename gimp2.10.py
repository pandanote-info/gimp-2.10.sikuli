# GIMP-2.10.8を起動し、スクリーンショットを取得するためのJythonのスクリプト。
# SikuliX-1.1.4 (2018-10-31_16:29)でのみテストを行っています。
# URL: https://pandanote.info/?p=3338
# Script to invoke GIMP-2.10.8 and to take a screenshot by it on SikuliX environment.
# This script is tested with SikuliX-1.1.4 (2018-10-31_16:29).
click("1542506859041.png")
wait(2)
click("1542509349902.png")
wait(10)
click(Pattern("1542510352713.png").targetOffset(-232,14))
wait(1)
click("1542510443808.png")
wait(1)
click("1542510526572.png")
wait(1)
click(Pattern("1542510591307.png").similar(0.81))
wait(1)
click("1542510609272.png")
type(Key.BACKSPACE)
type('10')
click(Pattern("1542510757822.png").similar(0.59).targetOffset(1,52))