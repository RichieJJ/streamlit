# streamlit

# spin up an ubuntu 20.04 vm; t2.micro; assign an EC2 Admin role

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

  URL: http://<public-ip>:8501
