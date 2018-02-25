i=1
ip_ext="130.82.237.82"
ip_int="130.82.238.173"
cache=20
pause=0.333
echo "running..."
while [ $i -lt 12 ]
do
    wget ${ip_int}:8080/images/$i.jpg -O img_drone/$i.jpg
    sleep 0.333
    let "i+=1"
    #let "i=i%cache"   
done

python3 detectColors.py

sshpass -p swissless scp img_output/output_graph.png pi@${ip_int}:cam-server/images/.
sshpass -p swissless scp img_output/panorama_img_output.jpg pi@${ip_int}:cam-server/images/. 
