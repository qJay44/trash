if [ "$#" -ne 2 ]; then
  echo "Error: expected 2 arguments: domain and port"
  exit 1
fi

IPS=$(nslookup $1 | awk '/^Address: /{print $2}')

while read -r ip; do
  echo "Testing $ip:$2"
  sudo tcpping -x 3 "$ip" "$2"
done <<< "$IPS"

