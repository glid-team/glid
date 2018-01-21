import platform

os_map = {
  "redhat":"redhat",
  "fedora":"redhat",
  "centos":"redhat",
  "scientific":"redhat",
  "scientific_cern":"redhat",
  "ascendos":"redhat",
  "cloud_linux":"redhat",
  "psbm":"redhat",
  "oracle_linux":"redhat",
  "oracle_vm_linux":"redhat",
  "oracle_enterprise_linux":"redhat",
  "amazon":"redhat",
  "xen_server":"redhat",
  "photon_os":"redhat",
  "huawei":"debian",
  "linux_mint":"debian",
  "ubuntu":"debian",
  "debian":"debian",
  "devuan":"debian",
  "suse_enterprise_server":"suse",
  "suse_enterprise_desktop":"suse",
  "open_suse":"suse",
  "suse":"suse",
  "gentoo":"gentoo",
  "archlinux":"archlinux",
  "manjarolinux":"archlinux",
  "mandrake":"mandrake",
  "mandriva":"mandrake",
  "mageia":"mandrake",
}

def osfamily():
  try:
    distro = platform.linux_distribution()
    return os_map[distro[0].lower()]
  except:
    return "N/A"

def arch():
  return platform.processor()
