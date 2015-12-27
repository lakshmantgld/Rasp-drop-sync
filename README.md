# Rasp-drop-sync
* This is an cronjob that runs on raspberry to sync with an dropbox account.
* The output of the cronjob can be mailed, thus providing an robust approach to sync with raspberry pi even without an public ip.
* Further, IFTTT can be configured on your mail account, and using webhooks can display cronjob's output to an web-page if needed.

### What this Repository does ?
- The **droprasp.py** checks for the dropbox account and copies everything to the local machine(Raspberry pi) for the first time.
- Later, If any new file is added, the cronjob checks for the changes in the dropbox account and updates the following:
  * If new file is added to dropbox, that will be downloaded to local machine.
  * If some files are deleted from dropbox, that will be deleted from the local machine too.
- The above file will be called periodically as it is set in crontab, and mails the output to the specified mail address.

### Installations and Configurations:
1. Install the dropbox python api using **pip install dropbox**.
2. Create an app(dropbox developer account), and get **application_key**, **application_secret**, **application_token**.
3. Store these credentials in the **config.yml** file.
4. For mailing to your external account, **sudo apt-get install mailutils**.
5. Give executable permission for **startscript.sh**.
6. Copy the given crontab task by using the command **crontab -e**.
7. Change the path of the **directories** in **dropbox.py**, where you need to sync your dropbox to local machine.

##### Installing and configuring SMTP for sending Mail:
1. sudo vim /etc/ssmtp/ssmtp.conf.
2. Hit “i” to enter Insert mode.
3. Uncomment FromLineOverride=YES by deleting the #.
4. Add the following to the file:
    - AuthUser=<user>@gmail.com
    - AuthPass=Your-Gmail-Password
    - mailhub=smtp.gmail.com:587
    - UseSTARTTLS=YES
5. save the file.
