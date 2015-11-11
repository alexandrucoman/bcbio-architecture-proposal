---
layout: default
title: "bcbio-nextgen-vm on Windows Azure"
---

###Introduction

A python toolkit providing best-practice pipelines for fully automated high throughput sequencing analysis. You write a high level configuration file specifying your inputs and analysis parameters. This input drives a parallel pipeline that handles distributed execution, idempotent processing restarts and safe transactional steps. The goal is to provide a shared community resource that handles the data processing component of sequencing analysis, providing researchers with more time to focus on the downstream biology.

More information can be found [here](https://bcbio-nextgen.readthedocs.org/en/latest/).

###Table of content

- I. [Environment setup](doc/environment-setup.html)
    - I.1. [Update the system](doc/environment-setup.html#i1-update-the-system)
    - I.2. [Install required packages](doc/environment-setup.html#i2-install-required-packages)
    - I.3. [Install azure client](doc/environment-setup.html#i3-install-azure-client)
    - I.4. [Install miniconda](doc/environment-setup.html#i4-install-miniconda)
    - I.5. [Install additional conda packages](doc/environment-setup.html#i5-install-additional-conda-packages)
- II. [Install bcbio-nextgen-vm](doc/install-bcbio-nextgen-vm.html)
    - II.1. [Add conda channel](doc/install-bcbio-nextgen-vm.html#ii1-add-conda-channel)
    - II.2. [Install bcbio-nextgen-vm package](doc/install-bcbio-nextgen-vm.html#ii2-install-bcbio-nextgen-vm-package)
- III. Setup Docker
    - III.1. [Install docker](doc/setup-docker#install-docker)
    - III.2. [Setup docker groups](doc/setup-docker#setup-docker-groups)
    - III.3. [Get bcbio/bcbio docker image](doc/setup-docker#get-bcbiobcbio-docker-image)
    - III.4. [Setup the datadir](doc/setup-docker#setup-the-datadir)
    - III.5. [Create a new docker image](doc/setup-docker#create-a-new-docker-image#create-and-upload-a-docker-image)
    - III.6. [Create and upload a docker image](doc/setup-docker)
    - III.7. [Upgrade docker image](doc/setup-docker#upgrade-docker-image)
- IV. [Setup azure environment](doc/setup-azure-environment.html)
    - IV.1. [Generate a new management certificate](doc/setup-azure-environment.html#generate-a-new-management-certificate)
    - IV.2. [Uploading managementCert.cer file to Windows Azure](doc/setup-azure-environment.html#uploading-managementcertcer-file-to-windows-azure)
    - IV.3. [Generate the private key](doc/setup-azure-environment.html#generate-the-private-key)
    - IV.4. [Create the elasticluster configuration file](doc/setup-azure-environment.html#create-the-elasticluster-configuration-file)