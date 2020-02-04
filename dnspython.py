#!/bin/python3

import socket
import dns.resolver

with open('file') as file:
    my_list = [line.strip() for line in file.readlines()]

resolver = dns.resolver.Resolver()
resolver.nameservers=[socket.gethostbyname('dns.name.server'), socket.gethostbyname('dns.name.server2')]

for domain in my_list:
    try:
        q = resolver.query(domain, 1)
        for rdata in q:
            print(f'{domain}: {rdata}')
    except dns.resolver.NoAnswer:
        print(f'{domain}: No answer')
