### ABOUT THIS PROJECT:

As a distro hopper, as sysadmin, as developer, one recurring problem was the wide packing standard, as the yearly [linux sucks](https://github.com/BryanLunduke/LinuxSucks) talks pointed out every year, packaging needs some love from the community.

At this stage to think that suddenly RedHat and Debian and Arch developers will sit down at one table and agree that they will use one and only packaging standard is is naive to think, so as always I suggest a [new standard](https://xkcd.com/927/) 

The long term plan for this project to shine and die, once it is widely used and a big enough mass is behind the idea, the hopefully will not be needed, but till then let's shine.

### FAQ:

**Q**:  How is this different then <insert random package manager\>?

**A**:  Strictly this is not a package manager, this is a wrapper for other package managers. The aim is to give instructions/ manuals not to store packages, just metadata, but for every platform

**Q**: Why do we even need this ? 

**A**: You might not need it, but why I think it will work is, because I seen that a lot of installation need hand-holding, and I think **glid** can offer that

**Q**: How do I contribute ?

**A**: Plenty of ways, see it [here](/contribute.md)

**Q**: Why **glid**?

**A**: The original idea was to make a **G**eneric **L**inux **I**nstaller **D**atabase, and BSD / OSX just come after, and I really want the installs to be "moving smoothly and easily" 

**Q**: What to expect how is this going to look like

**A**: First stage cli only, GUI is not in the scope right now

### The evil plan to take over the word:

 - acknowledge the problem exist
 - reach out all potential decision maker
 - collect list of tools which we aim to replace / overcome
 - clarify the scope how far we can/have to go
 - apply pressure with mass crowd to start the conversation
 - setup the agenda about the negotiation
 - create conversion plan, make sure there is commitment
 - write hands on tutorial, the best documentation possible

### Goals:

 - create a standard distro/lang independent package manager
 - free up dev time, less time spent on packaging
 - bigger penetration for new project by easy install option


### Tools:

 - distro
	- rpm ( yum ) 
	- deb ( dpkg, apt, aptitude )
	- snap
	- pkg
	- apk
	- tar.gz
	- brew
	- flatpack
	- appimage

 - language
	- php
		- pear
		- composer
		- packagist
	- python
		- pip
	- java
		- npm
		- bower
	- go
		- gopm
	- ruby
		- gem
		- bundler

 - tools / plugins / frameworks
	- chef
	- puppet
	- nagios
	- eclipse
	- wordpress
	- firefox
	- grafana

This is what **glid** need to know:

 - architecture aware
 - OS aware ( Mac / BSD / any flavour of Linux )
 - handle dependencies
 - pin versions
 - have extensive QA for package publish
 - must not try to host bin just instruction
 - per and after install "manual" commands
 - channel aware ( latest, stable, testing, etc )
 - written in widely know code ( go / python )
 - highly modular
 - Updates and clear uninstalls
