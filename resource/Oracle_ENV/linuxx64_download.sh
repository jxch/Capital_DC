#!/usr/bin/env bash

wget https://download.oracle.com/otn_software/linux/instantclient/1915000/instantclient-basic-linux.x64-19.15.0.0.0dbru.zip
unzip instantclient-basic-linux.x64-19.15.0.0.0dbru.zip
rm -rf instantclient-basic-linux.x64-19.15.0.0.0dbru.zip
mkdir ./instantclient-basic-linux.x64-19.15.0.0.0dbru/instactclient_19_15/network
mkdir ./instantclient-basic-linux.x64-19.15.0.0.0dbru/instactclient_19_15/network/admin
cp ./linuxx64/* ./instantclient-basic-linux.x64-19.15.0.0.0dbru/instactclient_19_15/network/admin/