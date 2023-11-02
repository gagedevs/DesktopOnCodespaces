git clone https://git.mollomm1.dev/Mollomm1/GamingOnCodespaces
cd GamingOnCodespaces
pip install textual
python3 installer.py
docker build -t gamingoncodespaces .
cd ..

sudo apt update
sudo apt install -y jq

mkdir Save
cp -r GamingOnCodespaces/root/config/* Save

json_file="GamingOnCodespaces/options.json"
if jq ".enablekvm" "$json_file" | grep -q true; then
    docker run -d --name=GamingOnCodespaces -e PUID=1000 -e PGID=1000 --device=/dev/kvm --security-opt seccomp=unconfined -e TZ=Etc/UTC -e SUBFOLDER=/ -e TITLE=GamingOnCodespaces -p 3000:3000 --shm-size="2gb" -v $(pwd)/Save:/config --restart unless-stopped gamingoncodespaces
else
    docker run -d --name=GamingOnCodespaces -e PUID=1000 -e PGID=1000 --security-opt seccomp=unconfined -e TZ=Etc/UTC -e SUBFOLDER=/ -e TITLE=GamingOnCodespaces -p 3000:3000 --shm-size="2gb" -v $(pwd)/Save:/config --restart unless-stopped gamingoncodespaces
fi
clear
echo "INSTALL FINISHED! Check Port Tab"