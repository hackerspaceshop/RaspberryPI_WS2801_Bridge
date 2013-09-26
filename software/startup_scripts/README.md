#move the file hackerspaceshop_ws2801 to /etc/init.d 
sudo mv hackerspaceshop_ws2801 /etc/init.d

# set executeable bit
sudo chmod +x /etc/init.d/ackerspaceshop_ws2801

# update init scripts (ignore warnings)
sudo update-rc.d hackerspaceshop_ws2801 defaults
