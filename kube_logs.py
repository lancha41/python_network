import subprocess
pod_name=input('type pod name: ')
container_name=input('container name (press enter if you need all logs from pod):')
main_command='kubectl get pods | grep '+pod_name
command=subprocess.run(main_command,shell=True,stdout=subprocess.PIPE,encoding='utf-8')
listc=command.stdout

kuber_log_command='kubectl logs '+pod_name+' -c '+container_name+' --timestamps > '+ container_name+'.log'
subprocess.run(kuber_log_command,shell=True)
