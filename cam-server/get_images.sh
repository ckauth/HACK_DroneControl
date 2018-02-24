i=1
cache=10
pause=0.333
while true;
do
	wget 130.82.238.173:8080/images/image.jpg -O $i.jpg
	sleep 0.333
	let "i+=1"
	let "i=i%cache"	
done
