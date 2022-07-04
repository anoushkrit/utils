
# uninstalling previous version of docker
m -r $HOME/.docker/desktop
sudo rm /usr/local/bin/com.docker.cli
sudo apt purge docker-desktop

#installing gnome terminal
sudo apt install gnome-terminal

echo   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# here download the docker-desktop from the website for your respective OS 
# then install that package 

sudo apt-get install ~/Downloads/docker-desktop-4.10.0-amd64.deb
sudo apt-get update

systemctl --user start docker-desktop

