# It lists every folder in the current directory
echo `ls -F | grep /$`

# Clip the first one and the last two characters of a variable
echo ${a:1:-2}
