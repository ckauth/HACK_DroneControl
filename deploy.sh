#!/bin/bash
PROJECT="swissless"

if [ $# -eq 0 ]
  then
        echo Deploying to Pi
        ADDRESS="130.82.238.173"
        USERNAME="pi"
        PASSWORD="xxx"
        SOURCETREE="/home/pi/"
        BINARYTREE="/home/pi/swissless/cmake"
        
        sshpass -p $PASSWORD ssh $USERNAME@$ADDRESS "rm -r ${SOURCETREE}${PROJECT}; mkdir ${SOURCETREE}${PROJECT}"
        sshpass -p $PASSWORD ssh $USERNAME@$ADDRESS "cd ${SOURCETREE}${PROJECT}; mkdir cmake"
        sshpass -p $PASSWORD scp ./main.c ./CMakeLists.txt "$USERNAME@$ADDRESS:$SOURCETREE$PROJECT"
        sshpass -p $PASSWORD ssh $USERNAME@$ADDRESS "cd ./swissless/cmake; cmake .. && make"
        sshpass -p $PASSWORD ssh $USERNAME@$ADDRESS "cd ${BINARYTREE}; sudo ./${PROJECT} '$DEVICE_CONNECTION_STRING'"
    else
        echo Deploying Locally
        rm -r ./cmake
        mkdir ./cmake
        cd ./cmake; cmake .. && make;
        sudo ./${PROJECT}
fi
