tableName="ip ps5_nat"
localIp=$(ip route show default | grep -oP '(?<=src\s)\d+(\.\d+){3}')

echo "Forwarding to [$localIp]"

if sudo nft list tables | grep -q "$tableName"; then
  sudo nft delete table $tableName
fi

sudo nft add table $tableName
sudo nft add chain $tableName postrouting { type nat hook postrouting priority 100 \; policy accept \; }
sudo nft add rule $tableName postrouting oifname "CloudflareWARP" masquerade

sudo sysctl -w net.ipv4.ip_forward=1

read -n 1 -s -r -p "Press any key to end..."

sudo sysctl -w net.ipv4.ip_forward=0
sudo nft delete table $tableName

