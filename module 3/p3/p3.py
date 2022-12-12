#!/usr/bin/env python

import ipaddress
from pcapfile import savefile

##########################
#### Assignment Input ####
##########################
nazir = "61.152.13.37"
mix = "95.235.155.122"
partner_count = 8
testcap = open('real.pcap', 'rb')

##########################
#### Helper Functions ####
##########################
capfile = savefile.load_savefile(testcap, layers=2, verbose=True)

def sum_ips(l):
  s = 0
  for ip in l:
    s += int(ipaddress.ip_address(ip))
  return s

def get_src(pkt):
  return pkt.packet.payload.src.decode("UTF8")

def get_dst(pkt):
  return pkt.packet.payload.dst.decode("UTF8")

##########################
#### Extract Batches #####
##########################
batches = list()
current_batch = set()
from_nazir = False
should_add = False
for pkt in capfile.packets:
  if should_add and not get_src(pkt) == mix:
    batches.append(current_batch.copy())
    current_batch.clear()
    should_add = False
    from_nazir = False
  if get_src(pkt) == nazir:
    from_nazir = True
  elif get_src(pkt) == mix and from_nazir:
    should_add = True
    current_batch.add(get_dst(pkt))

if from_nazir:
  batches.append(current_batch)

##########################
### Find Disjoint Sets ###
##########################
union_set = batches.copy().pop(0)
disjoint_sets = [union_set]
for s in batches:
  if union_set.isdisjoint(s):
    disjoint_sets.append(s)
    union_set = union_set.union(s)

assert(len(disjoint_sets) == partner_count)

##########################
##### Find Partners ######
##########################
for batch in batches:
  for i, dis in enumerate(disjoint_sets):
    no_others = all(map(lambda a: batch.isdisjoint(a) or a == dis, disjoint_sets))
    if no_others and dis.intersection(batch):
      disjoint_sets[i] = dis.intersection(batch)
  
  if all(map(lambda a: len(a) == 1, disjoint_sets)):
    break

flat_list = list()
for s in disjoint_sets:
  assert(len(s) == 1)
  print(s)
  flat_list.append(s.pop())

print(sum_ips(flat_list))
