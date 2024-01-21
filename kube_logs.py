import subprocess
command=subprocess.run('kubectl get pods | grep apollo',shell=True,stdout=subprocess.PIPE,encoding='utf-8')
listc=command.stdout
for line in listc.split():
    if "apollo" in line:
        log_command='kubectl logs '+line+' -c container --timestamps > '+line+'.log'
        subprocess.run(log_command,shell=True)
