Above are folders with working Dockerfiles for ubuntu and debian.
For some reason sometimes it fail to [build](https://hub.docker.com/r/oookotooo/fake-switches/builds/), without making any changes  

Full Description for [oookotooo/fake-switches](https://hub.docker.com/r/oookotooo/fake-switches/)
============================================
This docker repository have 2 tags: [`latest`](https://github.com/oookotooo/SoftServe-1/blob/master/fake-switches-dockerfiles/fake-sw-debian/Dockerfile) (based on debian python 2.7.12 image) and [`ubuntu`](https://github.com/oookotooo/SoftServe-1/blob/master/fake-switches-dockerfiles/fake-sw-ubuntu/Dockerfile).  
Use any of this, `latest` should work fine.
To run it:
```
docker run -p 11001:11001 -d oookotooo/fake-switches
ssh root@localhost -p 11001
```
or just  
`docker run -Pd oookotooo/fake-switches`  
  
if you want special config or non-cisco router, do:  
```
docker run -P -it --entrypoint=/bin/bash oookotooo/fake-switches
vi start.py
```
Change here everything as you wish and run.  
```
. .tox/py27/bin/activate
python start.py &
```

Guide for installing it locally (note, it also could fail once, but go ok next time):  
====================================================================================

We will install it in /tmp/app  
  
installing basic stuff (note, fake-switches 1.1.6 does not work with python 3):  
```
sudo su
apt-get update
apt-get install -y git 
```
let's clone git repo
```
sudo git clone -q https://github.com/internap/fake-switches.git
cd /tmp/app/fake-switches
```
this stuff needed for python and fix InSecurePlatformWarning:  
`apt-get install -y python-lxml python-dev libffi-dev libssl-dev telnet telnetd python python-pip `
now install pip reqiuerements: 
```
pip install tox
pip install netaddr
pip install tftpy
pip install pycrypto
pip install Twisted
pip install pyasn1
pip install nose
pip install mock
pip install pyhamcrest
pip install pexpect
pip install flexmock
pip install ncclient
```
`sudo python setup.py install`  
fix SSHException: Signature verification (ssh-rsa) failed  
`apt-get install -y openssl`  
switch repo to latest stable release  
`git checkout tags/1.1.6`  
installation process in /tmp/app/fake-switches, it is long process, about 10 min on i5  
`tox -r`  
now let's generate router (cisco for this example)  
`vi start.py`  
insert this code config, or any other  
```
from twisted.internet import reactor
from fake_switches.switch_configuration import SwitchConfiguration, Port
from fake_switches.ssh_service import SwitchSshService
from fake_switches.cisco.cisco_core import CiscoSwitchCore

ssh_service = SwitchSshService(
    ip="127.0.0.1",
    ssh_port=11001,
    switch_core=CiscoSwitchCore(SwitchConfiguration("127.0.0.1", "my_switch", ports=[Port("FastEthernet0/1"), Port("FastEthernet0/2"), Port("FastEthernet0/3")])))
ssh_service.hook_to_reactor(reactor)
print('Starting reactor')
reactor.run()
```
now start reactor!
```
. /tmp/app/fake-switches/.tox/py27/bin/activate
python /tmp/app/fake-switches/start.py &
```
now you can ssh to router:  
`ssh root@localhost -p 11001`  
The default password should be "root". Then the enable password is "", simply press enter.  
