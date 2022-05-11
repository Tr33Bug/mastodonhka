# BulletinBOT
> Mastodon BOT to post content from newsbulletinboard from Hochschule Karlsruhe on projekt-mastodon.h-ka-iwi.de


## Setup as *cronjob*

### preperation

1. check or python3

```bash
python3 --version
```

### installation

1. clone the git repository

```bash
git clone git@github.com:Tr33Bug/mastodonhka.git
cd ./mastodonhka
```
2. create a `config.py` for the mastodon token in mastodonhka folder

```bash
echo "MASTODON_TOKEN = \"\"" > config.py
vim ./config.py
# or
nano ./config.py
```

3. enter the token `XXXXXXXXXX`, logfilepath and sleeptimer

```
MASTODON_TOKEN = `XXXXXXXXXX`
LOGFILE = PathToLogfile
SLEEPTIME = 5
```

save and close the file.

4. install python packages

```bash
python3 -m pip install requests
```
more info on the request module: https://docs.python-requests.org/en/latest/
5. remember path where the script is

```
pwd
```
for example: .../Downloads/mastodonhka

6. setup a cronjob for the script

```bash
crontab -e
```

add the path of the *bulletinBotCron.py*-File to Bottom: 

```
5 * * * * .../Downloads/mastodonhka/bulletinBotCron.py
```

This cronjob configuration relaunches the script every 5 minutes.

! If you want to change the Timer, you have to change the SLEEPTIME in the configuration and the cronjob.

reed more about cronjob setup here: https://pimylifeup.com/cron-jobs-and-crontab/


## Setup with *systemd* (deprecated)
If you want to use systemd, you have to use the *bulletinBotSysD.py* version of the bot.

1. install *systemd* and check the version

```bash
sudo apt-get install -y systemd
systemd --version
```

2. create a service config file for systemd

```bash
cd /etc/systemd/system/
touch bulletinBot.service
```

6. copy the configuration in the file and change the path to your user (/home/\<USERNAME\>/bulletinBOT.py)

```
[Unit]
Description=BulletinBOT for Mastodon HKA news report
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

9. check the status

```bash
sudo systemctl status bulletinBot.service
```

10. finish
- in-depth tutorial: https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267
- more help on systemd: https://wiki.archlinux.org/title/Systemd

### debugging
the logs from the bulletinBot.py are in the home from root in the *botLog.txt*

```bash
sudo -i
cd ~
cat botLog.txt#or 
tail -f botLog.txt
```
