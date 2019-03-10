<p align="center"><a href="https://github.com/absolum1"
target="_blank"><br><img width="200" src="https://absolum.nl/assets/images/absolum-min-1014x789.png"></a></p>


<h1 align="center">Apache-VHC</h1>


<p align="center">Easy to use Apache (sub)domain creator</p>


<p align="center"> 
<a href="https://absolum.nl"><img src="https://img.shields.io/badge/website-absolum.nl-lightgrey.svg" alt="Website"></a>
<a href="https://github.com/absolum1"><img src="https://img.shields.io/badge/build-success-lightgrey.svg" alt="Build"></a>
<a href="https://absolum.nl/Licenses"><img src="https://img.shields.io/badge/license-MIT-lightgrey.svg" alt="License"></a>
</p>


## Tags
- :page_facing_up: Apache
- :computer: Ubuntu tested
- :snake: Python
- 🎉 Open source


## Apache-VHC
Apache-VHC is a spin of [avhCreator](https://github.com/rakibtg/Apache-Virtual-Hosts-Creator/blob/master/avhCreator.py) And it is used to automate the creation and setup of new (sub)domains on Apache. 

## Prerequisites
1. Apache server configured [guide](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-ubuntu-16-04)
2. Dns setup correctly (pointing at your server)
3. Python installed (```sudo apt-get install python```)

## Installation
1. ```sudo apt-get update```
2. ```wget https://raw.githubusercontent.com/Absolum1/Apache-VHC/master/VHC.py```
3. That's it

## Usage
1. ```sudo python VHC.py```
2. Answer the questions

## Bonus
- Setup [certbot](https://certbot.eff.org/lets-encrypt/ubuntubionic-apache) for easy ssl certificates

