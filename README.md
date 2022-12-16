# streamlit

# spin up an ubuntu 20.04 vm; t2.micro; assign an EC2 Admin role
# Install Docker using the repository and Update the apt package index and install packages to allow apt to use a repository over HTTPS:
# sudo apt-get update 
# sudo chmod a+r /etc/apt/keyrings/docker.gpg
# sudo apt-get update

# Add Docker’s official GPG key:
# sudo mkdir -p /etc/apt/keyrings
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Use the following command to set up the repository:
# echo \
#   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
#   $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null --
  

# Install Docker Engine and Update the apt package index: 
sudo apt-get update
sudo chmod a+r /etc/apt/keyrings/docker.gpg
sudo apt-get update

# Install Docker Engine, containerd, and Docker Compose.
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Verify that the Docker Engine installation is successful by running the hello-world image:
sudo docker run hello-world

# Create a docker image from the Dockerfile
docker build -t streamlit .

# See streamlit image
docker images

# Create a container from the image
docker run -p 8501:8501 streamlit

# If all went well, you should see an output similar to the following:
$ docker run -p 8501:8501 streamlit

  You can now view your Streamlit app in your browser.

  URL: http://<localhost-public-ip>:8501
