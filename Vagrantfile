# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.hostname = "pillow-bug"
  config.vm.box = "debian/buster64"
  config.vm.provision "pillow", type: "shell", path: "pillow.sh"
  config.vm.synced_folder ".", "/vagrant", type: "rsync",
  rsync__verbose: true
end
