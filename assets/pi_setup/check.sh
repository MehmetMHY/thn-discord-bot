up () {
	sudo apt update
	sudo apt upgrade
	sudo apt autoremove
	sudo apt clean
}

cat << EOF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃ RASPBERRY PI SYSTEM QUICK CHECKUP ┃
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF
echo

echo "➤Who(s):"
who
echo

echo "➤PYDF:"
pydf
echo

echo "➤NEOFETCH:"
neofetch --color_blocks --off | grep 'OS\|Packages\|CPU\|Memory\|Shell'
echo

echo "➤UPTIME:"
uptime
echo

echo "➤PY3-PROCS:"
ps -fA | grep "python3" | grep -v 'grep'
echo

echo "➤TEMP:"
vcgencmd measure_temp
echo

# add -u param to also update & upgrade APT
if [ "$1" == "-u" ]
then
	echo "➤APT 'UP' COMMAND / UPDATE➜UPGRADE➜AUTOREMOVE➜CLEAN"
	echo
	up
	echo
fi


