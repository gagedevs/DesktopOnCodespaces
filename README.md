# GamingOnCodespaces (Beta)

a better version of https://codeberg.org/Mollomm1/W10-On-Github-Codespaces

> ⚠️ This project is currently a work in progress and is still unfinished. While I'm actively working on it and making progress, there may still be bugs and incomplete features. ⚠️

# Supported Stuff

* 1080p 60fps

* Sound

* Windows apps (wine)

* Browsering (Brave and Firefox included!)

* Home Persistance (You keep your files!)

# Use

it's very simple to install.

clone the repo
```
git clone https://git.mollomm1.dev/Mollomm1/GamingOnCodespaces
cd GamingOnCodespaces
```


build the container (take long 5-10 minutes)
```
docker build -t gamingoncodespaces .
```

then go back to your home directory
```
cd ..
```

initialise the default Persistance directory
```
mkdir Save
cp -r GamingOnCodespaces/root/config/Desktop Save
```

and after you can do 
```
docker run --name=GamingOnCodespaces -e PUID=1000 -e PGID=1000 --security-opt seccomp=unconfined -e TZ=Etc/UTC -e SUBFOLDER=/ -e TITLE=GamingOnCodespaces -p 3000:3000 --shm-size="2gb" -v $(pwd)/Save:/config --restart unless-stopped gamingoncodespaces
```