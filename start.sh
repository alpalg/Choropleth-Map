echo "Hello, this script install all needed packages."
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
echo 'deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen' | sudo tee  /etc/apt/sources.list.d/mongodb.list
sudo apt-get -y update
sudo apt-get -y install mongodb-10gen
sudo /etc/init.d/mongodb start
sudo apt-get -y install wget
sudo apt-get -y install python
sudo python -m pip install flask
sudo python -m pip install pymongo
wget http://jsonstudio.com/wp-content/uploads/2014/02/world_bank.zip -P /tmp/
sudo unzip /tmp/world_bank.zip -d /tmp/
cd /tmp/
sudo mongoimport --db world_bank --collection world --file /tmp/world_bank.json
