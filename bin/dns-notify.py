#!/usr/bin/env python3
## -*- coding: utf-8 -*- vim:shiftwidth=4:expandtab:
##
## DNS: Send a DNS zone changes notify message to a slave DNS contents server
## Copyright (c) 2020 SATOH Fumiyasu @ OSS Technology Corp., Japan
##
## License: GNU General Publice License version 3
##

import sys
import socket
import dns.message
import dns.rdatatype
import dns.opcode
import dns.flags
import dns.query


if len(sys.argv) < 3:
    print("Usage: %s NAMESERVER ZONE" % (sys.argv[0]))
    sys.exit(1)

(ns_name, zone) = sys.argv[1:3]
ns_ip = socket.gethostbyname(ns_name)
notify = dns.message.make_query(zone, dns.rdatatype.SOA)
notify.set_opcode(dns.opcode.NOTIFY)
notify.flags -= dns.flags.RD
response = dns.query.udp(notify, ns_ip, timeout=5)
print(response)
sys.exit(0)
