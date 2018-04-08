
> As a distro hopper/sysadmin/developer, one recurring problem has always been *plethora of packaging standards* used to set up an environment. As the yearly [Linux sucks](https://github.com/BryanLunduke/LinuxSucks) talks make light of - packaging needs some love from the community.

## About this project

The aim of `glid` is to simplify installing Linux packages. Unfortunately at this stage it seems too optimistic to believe that Red Hat, Debian and Arch developers will be able to come together and agree on a single standard, and so in it's place we suggest a [new standard](https://xkcd.com/927/).

## FAQs
**Q**:  How is this different than <insert random package manager\>?

**A**:  Strictly `glid` is not a package manager, but simply a wrapper for other package managers, driven by a repository of metadata for a wide range of Linux packages (sort of like [@types](https://github.com/DefinitelyTyped/DefinitelyTyped) for TypeScript). Each entry in the repository will contain the required information to install the package on any Linux distribution.

-----

**Q**: Why do we even need this?

**A**: The aim of `glid` is to save you time. Why google how to install package `x` on distribution `y` when the same problem has been solved many hundreds of times before.

-----

**Q**: OK I get it - how can I contribute ?

**A**: Plenty of ways, see it [here](/contribute.md)

----

**Q**: Why `glid`?

**A**: This tool aims to provide a **G**eneric **L**inux **I**nstaller **D**atabase (with BSD and OSX coming after)

----

**Q**: How does `glid` work?

**A**: Initially as a CLI only. A GUI is currently out of scope


## The Roadmap (or, *how to conquer the world*)

 - Acknowledge the problem exists
 - Reach out all potential decision makers
 - Collate a list of tools which we aim to replace/overcome
 - Clarify the scope of the project (Distros & Packages)
 - Through public adoption, begin to apply pressure on distro providers to take ownership of the problem
 - Manage the discussion. Bring actors to the table and ensure there is real commitment
 - Develop outstanding documentation and help resources

## Intended Goals

 - Create a standard distro/language independent package manager
 - Free up developer time spent on package management
 - Bigger penetration for new project by easy install option


## Tools

Here's a rough light of the all the things which `glid` aims to unify:

 - Distros
	- rpm ( yum )
	- deb ( dpkg, apt, aptitude )
	- snap
	- pkg
	- apk
	- tar.gz
	- brew
	- flatpack
	- appimage

 - Languages
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

------

In order to do this, `glid` needs to be:

 - Architecture aware
 - OS aware (Mac / BSD / any flavour of Linux)
 - Able to handle dependencies
 - Able to pin versions
 - Have extensive QA for packages published
 - Channel aware (latest, stable, testing, etc)
 - Written in a clear and widely used language (e.g. go/python)
 - Highly modular
 - Able to clearly support both *updates* and *uninstalls*
 - Able to handle lifecycle hooks (e.g. "post install")

It should *not* be:
 - A host of binaries, simply instructions
