# #ff0000 #ff0000 HARDCODED #ff0000 #ff0000

SCRIPT_DIR=$(dirname "$(realpath "$0")")
cd "$SCRIPT_DIR" || { echo "Cound not enter directory [${SCRIPT_DIR}]"; exit 1; }

ZAPRET_HOME=$HOME/zapret-discord-youtube-linux
ZAPRET_LATEST=$ZAPRET_HOME/zapret-latest

table_name="ip ps5_nat"
tcp_ports="80, 443, 1024-65535"
udp_ports="443, 1024-65535"
queue_num=220
oif_clause="oifname \"wlan0\""

if sudo nft list tables | grep -q "$table_name"; then
  sudo nft delete table $table_name
fi

sudo nft add table $table_name
sudo nft add chain $table_name postrouting { type nat hook postrouting priority 100\; policy accept\; }
sudo nft add rule $table_name postrouting $oif_clause masquerade

sudo nft add chain $table_name forward { type filter hook forward priority 0\; policy accept\; }
sudo nft add rule $table_name forward $oif_clause meta mark != 0x40000000 tcp dport {$tcp_ports} counter queue num $queue_num bypass
sudo nft add rule $table_name forward $oif_clause meta mark != 0x40000000 udp dport {$udp_ports} counter queue num $queue_num bypass

cp -rT $ZAPRET_LATEST/lists-rl $ZAPRET_LATEST/lists
sudo sysctl -w net.ipv4.ip_forward=1

sh $ZAPRET_HOME/main_script.sh <<< $'y\n1\n3'

cp -rT $ZAPRET_LATEST/lists-default $ZAPRET_LATEST/lists
sudo sysctl -w net.ipv4.ip_forward=0

sudo nft delete table "ip ps5_nat"


