for (( i=0; i < 350; i++));
do top -b -n 1 -p `pgrep -f bidi-proxy-gw` | tail -1 | awk '{print $9/32}' >> cltCPU.log
   top -b -n 1 -p `pgrep -f bidi-proxy-gw` | tail -1 | awk '{print $10}'  >> cltMEM.log
   sleep 6;
done
