---
title: "Ansible Lab-setup"
description: "Ansible is an open source automation tool that simplifies the management of servers, applications, and network devices. In this blog, we will discuss how…"
lang: other
categories: ["Ansible"]
author: "Shakti Das"
pubDate: 2023-04-04T08:10:08Z
legacy: true
wpId: 3567
---

Ansible is an open-source automation tool that simplifies the management of servers, applications, and network devices. In this blog, we will discuss how to set up an Ansible lab environment for testing and learning purposes.

Before we begin, it is important to note that Ansible can be installed on a variety of operating systems such as Linux, macOS, and Windows. For this lab setup, we will be using a Linux-based operating system.

Step 1: Install VirtualBox

VirtualBox is a free and open-source virtualization software that allows you to create and manage virtual machines. Install VirtualBox on your host machine by downloading the appropriate package for your operating system from the VirtualBox website.

Step 2: Download a Linux Image

Download a Linux image such as Ubuntu or CentOS from the respective website. Choose a minimal installation image to keep the installation size small.

Step 3: Create a Virtual Machine

Open VirtualBox and click on "New" to create a new virtual machine. Give the virtual machine a name, select the Linux image that you downloaded, and configure the desired amount of RAM and storage space.

Step 4: Install Linux on the Virtual Machine

Start the virtual machine and follow the installation prompts to install Linux on the virtual machine. Once the installation is complete, log in to the Linux environment.

Step 5: Install Ansible

Install Ansible on the Linux virtual machine by running the following command in the terminal:

```yaml
sudo apt-get install ansible
```

This command will install Ansible and its dependencies on the virtual machine.

Step 6: Configure the Inventory File

Create an inventory file that contains the list of hosts that Ansible will manage. The inventory file can be created in the /etc/ansible/hosts file on the Linux virtual machine.

```yaml
webserver ansible_host=192.168.1.100 ansible_user=user ansible_ssh_pass=password
```

This example inventory file defines a group called "web" that contains a single host with the IP address 192.168.1.100. The ansible\_user and ansible\_ssh\_pass variables define the username and password that Ansible will use to connect to the host.

Step 7: Create a Playbook

Create a playbook that contains a set of tasks that Ansible will perform. Playbooks are written in YAML format and can be created in any text editor.

```yaml
yaml
- name: Install Apache web server
  hosts: web
  become: yes
  tasks:
  - name: Install Apache
    apt:
      name: apache2
      state: present
```

This example playbook defines a single task that installs the Apache web server on the host defined in the "web" group.

Step 8: Run the Playbook

Run the playbook by running the following command in the terminal:

```yaml
ansible-playbook playbook.yml
```

This command will execute the playbook and perform the tasks defined in the playbook on the hosts defined in the inventory file.

Conclusion:

Setting up an Ansible lab environment is a great way to learn and test Ansible without affecting production systems. By following these steps, you can quickly set up a virtual machine with Ansible installed and start automating tasks. Once you have mastered the basics, you can explore more advanced features of Ansible and create complex playbooks to automate more complex tasks.
