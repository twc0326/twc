# Install flask on EC2 
# Either add "sudo" before all commands or use "sudo su" first
# Amazon Linux 2023

#!/bin/bash
yum update -y
yum install git -y
git clone https://github.com/twc0326/twc.git
cd twc
yum install python-pip -y
pip3 install flask pymysql boto3
python3 EmpApp.py
