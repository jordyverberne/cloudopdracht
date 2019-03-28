# klautopdracht


checkin en uit tijden doorgeven met:
curl https://<ipaddress>:5000/checkinout -k -d '<kaartid>' -X PUT
curl https://192.168.1.101:5000/checkinout -k -d 'kaartid=73288188241L' -X PUT

gegevens opvragen:
curl https://192.168.1.101:5000/query -k -d 'kaartid=73288188241L' -X GET
