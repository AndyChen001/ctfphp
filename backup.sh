#!/bin/bash

back_dir="/var/www/html/"
back_file="/xxx/web.tar"
back_file_old="/xxx/web_old.tar"


while true;do

if [ ! -f "$back_file" ]; then 
    tar -cf "$back_file" "$back_dir"
    echo "Backup Sucess!"
else
    mv "$back_file" "$back_file_old"
    echo "Mv Backup Sucess!"
    tar -cf "$back_file" "$back_dir"
    echo "Backup Sucess!"
fi

sleep 2m

done
