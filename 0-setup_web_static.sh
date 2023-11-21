#!/usr/bin/env bash
# sets the web servers for the deployment of web_static

trap 'exit 0' ERR

if ! command -v nginx &> /dev/null; then
	sudo apt update
	sudo apt install nginx -y
