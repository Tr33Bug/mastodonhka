# BulletinBOT
> Mastodon BOT to post content from newsbulletinboard from Hochschule Karlsruhe on projekt-mastodon.h-ka-iwi.de

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

1. clone the git repository
```bash
git clone git@github.com:Tr33Bug/mastodonhka.git
cd ./mastodonhka
```
2. create a `config.py` for the mastodon token
```bash
echo "MASTODON_TOKEN = \"\"" > config.py
vim ./config.py
# or
nano ./config.py
```

3. enter the token `XXXXXXXXXX`
```
MASTODON_TOKEN = "XXXXXXXXXX"
```

4. install python packages
```bash
python3 -m pip install requests
```
more info on the request-module: https://docs.python-requests.org/en/latest/

5. create a service config file for systemd
```bash
cd /etc/systemd/system/
touch bulletinBot.service
```

6. copy the configuration in the file and change the path to your usr (/home/\<USERNAME\>/bulletinBOT.py)
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

7. reload the daemon and enable the service
```bash
sudo systemctl daemon-reload
sudo systemctl enable bulletinBot.service
```

8. start the service
```bash
sudo systemctl start bulletinBot.service
```

9. finish, check status
```bash
sudo systemctl status bulletinBot.service
```
in depth tutorial: https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267
more help on systemd: https://wiki.archlinux.org/title/Systemd
