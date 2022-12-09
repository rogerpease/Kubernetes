#!/usr/bin/env python3 

import os 

FoundPod = False

from kubernetes import client, config

config.load_kube_config()

v1=client.CoreV1Api()
ret = v1.list_pod_for_all_namespaces(watch=False)
output = [] 
for i in ret.items:
    if "hellow" in i.metadata.name:
      os.system("kubectl exec --stdin --tty "+i.metadata.name + " -- bash") 
      FoundPod = True

    output.append("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

if not FoundPod:
  print("\n".join(output))
