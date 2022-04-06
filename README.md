# BulletinBOT

## preperation
1. install systemd and check version
```bash
sudo apt-get install -y systemd
systemd --version
```
2. check for python3
```bash
python3 --version
```

## installation
0. install python packages
```bash
python3 -m pip install requests
```
more info on the request-module: https://docs.python-requests.org/en/latest/

1. create a service config file for systemd
```bash
cd /etc/systemd/system/
touch bulletinBot.service
```
2. copy the configuration in the file and change the path to your usr (/home/\<USERNAME\>/bulletinBOT.py)

```
[Unit]
Description=BulletinBOT for Mastodon HKA newsreport
After=multi-user.target

[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 /home/<USERNAME>/bulletinBOT.py

[Install]
WantedBy=multi-user.target
```
3. reload the daemon and enable the service
```bash
sudo systemctl daemon-reload
sudo systemctl enable bulletinBot.service
```

4. start the service
```bash
sudo systemctl start bulletinBot.service
```
5. finish, check status
```bash
sudo systemctl status bulletinBot.service
```
