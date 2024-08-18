for i in $(seq 20 -1 2); do ssh -t root@172.16.$i.1 "sleep 360 && poweroff"; done
