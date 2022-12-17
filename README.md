# streamlit

# spin up an ubuntu 20.04 vm; t2.micro; assign an EC2 Admin role

# Install Docker Engine and Update the apt package index: 

sudo apt-get update

sudo apt-get install     ca-certificates     curl     gnupg     lsb-release

sudo mkdir -p /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  
sudo apt-get update

sudo chmod a+r /etc/apt/keyrings/docker.gpg

sudo apt-get update

# Install Docker Engine, containerd, and Docker Compose.
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Verify docker was succesfully installed
sudo docker run hello-world

# create a Dockerfile in the VM and paste the content of the "Dockerfile" in this repo there, save and quit - :wq enter.
vim Dockerfile

# Create a docker image from the Dockerfile
docker build -t streamlit .

# See streamlit image
docker images

# Create a container from the image
docker run -p 8501:8501 streamlit

# If all went well, you should see an output similar to the following:
$ docker run -p 8501:8501 streamlit

  You can now view your Streamlit app in your browser.

  URL: http://<public-ip>:8501
