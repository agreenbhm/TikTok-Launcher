if ! [ -f /data/data/com.termux/files/home/adb_port.txt ]
then
  echo "12345" > /data/data/com.termux/files/home/adb_port.txt
fi
PORT=$(cat /data/data/com.termux/files/home/adb_port.txt)
echo $PORT
echo $1
/data/data/com.termux/files/usr/bin/adb connect localhost:$PORT | grep refused
if [ $? == 1 ]
then
  /data/data/com.termux/files/usr/bin/adb shell am start --user 10 $1
  /data/data/com.termux/files/usr/bin/adb disconnect
else
  /data/data/com.termux/files/usr/bin/python3 /data/data/com.termux/files/home/launch_tiktok.py $1
fi
