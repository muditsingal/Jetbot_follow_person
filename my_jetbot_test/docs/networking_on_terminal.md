# A guide to connect to wireless networks using ubuntu terminal

[Important link](https://blog.rottenwifi.com/ubuntu-connect-to-wifi-terminal/)

### NMCLI or (Network Manager Command-Line)
This is an easy-to-use yet powerful command line tool, using which, you can see available networks, connect to a network and even forget/delete saved networks.

#### Most frequently used commands:

`nmcli dev status`: This command shows the status of your network interfaces, i.e. if you have the Intel8265 wifi card installed then you will see it using this command.
Following is a sample output:

```
DEVICE   TYPE      STATE        CONNECTION
wlan0    wifi      connected    hotspot 2
docker0  bridge    connected    docker0
eth0     ethernet  unavailable  --
l4tbr0   bridge    unmanaged    --
dummy0   dummy     unmanaged    --
rndis0   ethernet  unmanaged    --
usb0     ethernet  unmanaged    --
lo       loopback  unmanaged    --
```


`nmcli radio wifi`: This command shows whether wifi is enabled or disabled for your jetson nano

`nmcli radio wifi on`:  This command turns on the wifi of your jetson nano, if proper hardware is present

`nmcli dev wifi list`: This command shows all the available wifi networks that are detected by your device

`sudo nmcli dev wifi connect your_wifi_name password your_wifi_password`: This command can be used to connect to any wifi network ('your_wifi_name' is the network-SSID)

`sudo nmcli connection delete your_wifi_name`: This command deletes(forget) an already existing connection. You can use this if you are having trouble connecting to an exising network.

[A complete guide for nmcli](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-configuring_ip_networking_with_nmcli)
