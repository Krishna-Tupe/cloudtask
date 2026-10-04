#!/bin/bash
# Run on the EC2 instance (Ubuntu) after: ssh -i key.pem ubuntu@<EC2_PUBLIC_IP>
sudo apt update && sudo apt install -y python3-pip python3-venv git
git clone https://github.com/<your-username>/cloudtask.git && cd cloudtask
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
nohup gunicorn -b 0.0.0.0:5000 app:app &
echo "Open http://<EC2_PUBLIC_IP>:5000 (allow port 5000 in Security Group)"
