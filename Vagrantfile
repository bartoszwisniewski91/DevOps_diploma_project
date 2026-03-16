# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Używamy stabilnego obrazu Ubuntu 22.04 LTS (Jammy)
  config.vm.box = "ubuntu/jammy64"

  # ==========================================
  # Maszyna 1: Serwer Aplikacyjny (Flask + Runner)
  # ==========================================
  config.vm.define "app-server" do |app|
    app.vm.hostname = "app-server"
    # Przypisanie statycznego adresu IP w prywatnej sieci
    app.vm.network "private_network", ip: "192.168.0.100"
    
    # Forwardowanie portów (aby móc testować aplikację w przeglądarce gospodarza)
    app.vm.network "forwarded_port", guest: 5000, host: 5000, id: "flask"

    app.vm.provider "virtualbox" do |vb|
      vb.name = "devops-app-server"
      vb.memory = "1024" # 1GB RAM wystarczy dla Flaska i Runnera
      vb.cpus = 1
    end
  end

  # ==========================================
  # Maszyna 2: Serwer Monitoringu (Grafana, Prometheus, Loki)
  # ==========================================
  config.vm.define "monitor-server" do |monitor|
    monitor.vm.hostname = "monitor-server"
    monitor.vm.network "private_network", ip: "192.168.56.11"
    
    # Forwardowanie portów do zarządzania z poziomu przeglądarki gospodarza
    monitor.vm.network "forwarded_port", guest: 3000, host: 3000, id: "grafana"
    monitor.vm.network "forwarded_port", guest: 9090, host: 9090, id: "prometheus"

    monitor.vm.provider "virtualbox" do |vb|
      vb.name = "devops-monitor-server"
      vb.memory = "2048" # Stos monitoringu potrzebuje więcej pamięci RAM
      vb.cpus = 2
    end
  end
end