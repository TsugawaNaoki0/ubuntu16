OS : Ubuntu 18.04.1 LTS


dpkg-reconfigure tzdata


apt-get update
apt-get install ntpdate
ntpdate pool.ntp.br
apt-get install ntp
date


apt-get update
apt-get install ntpdate
ntpdate pool.ntp.br
apt-get install ntp
date


apt-get update
apt-get install software-properties-common
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
add-apt-repository 'deb [arch=amd64,i386] http://nyc2.mirrors.digitalocean.com/mariadb/repo/10.2/ubuntu artful main'
apt-get update
apt-get install mariadb-server mariadb-client


mysql -u root -p


CREATE DATABASE glpi CHARACTER SET UTF8 COLLATE UTF8_BIN;
CREATE USER 'glpi'@'%' IDENTIFIED BY 'kamisama123';
GRANT ALL PRIVILEGES ON glpi.* TO 'glpi'@'%';
quit;


apt-get install apache2 php libapache2-mod-php
apt-get install php-json php-gd php-curl php-mysql php-mbstring
apt-get install php-xml php-cli php-imap php-ldap php-xmlrpc php-apcu
updatedb
locate php.ini
vi /etc/php/7.0/apache2/php.ini


file_uploads = On
max_execution_time = 300
memory_limit = 256M
post_max_size = 32M
max_input_time = 60
max_input_vars = 4440


service apache2 stop
service apache2 start
service apache2 status


mkdir /downloads
cd /downloads
wget https://github.com/glpi-project/glpi/releases/download/9.2.2/glpi-9.2.2.tgz
tar -zxvf glpi-9.2.2.tgz
ls


mkdir /var/www/html/glpi
mv glpi/* /var/www/html/glpi
chown www-data.www-data /var/www/html/glpi/* -R


vi /etc/apache2/conf-available/glpi.conf


<Directory /var/www/html/glpi>
AllowOverride All
</Directory>

<Directory /var/www/html/glpi/config>
Options -Indexes
</Directory>

<Directory /var/www/html/glpi/files>
Options -Indexes
</Directory>


a2enconf glpi


service apache2 stop
service apache2 start


URL  : localhost
User : glpi
Pass : kamisama123
