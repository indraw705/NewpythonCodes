import paramiko

username = "inarvekar"
password = "Sakal@123!@#"


def check_status(hostname):
    print(
        f"{hostname} : policy version = {check_manifest(hostname)} and agent Version = {check_agent_version(hostname)} ")


def check_manifest(hostname):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username, password=password)
    except :
        print(f"[!] Cannot connect to the SSH Server {hostname}")

    ls_command = "sudo ls /usr/local/qualys/cloud-agent/edr/manifests/"
    output = ""
    stdin, stdout, stderr = client.exec_command(ls_command)
    stdout = stdout.readlines()
    for line in stdout:
        output = output + line
    policy_version = ""
    cat_command = "sudo cat /usr/local/qualys/cloud-agent/edr/manifests/" + output.strip() + " | grep policyVersion"
    # print(cat_command)
    stdin, stdout, stderr = client.exec_command(cat_command)
    stdout = stdout.readlines()
    for line in stdout:
        policy_version = policy_version + line
    if policy_version != "":
        return policy_version.strip()
    else:
        print("There was no output for this command")
    client.close()


def check_agent_version(hostname):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username, password=password)
    except:
        print("[!] Cannot connect to the SSH Server")
    client.exec_command("sudo su")
    version_command = "rpm -qa | grep qualys-cloud-agent"
    # print(cat_command)
    stdin, stdout, stderr = client.exec_command(version_command)
    stdout = str(stdout.readlines())
    agent_version = stdout.split("-")
    agent_version = agent_version[3] + "-" + agent_version[4]
    agent_version = agent_version[0:9]
    if agent_version != "":
        return agent_version.strip()
    else:
        print("There was no output for this command")
    client.close()


check_status("masifdatlob01.p01.eng.sjc01.qualys.com")
check_status("dst02.p01.eng.sjc01.qualys.com")
check_status("kubeetcd02.p01.eng.sjc01.qualys.com")
check_status("crsmongodb01.p01.eng.sjc01.qualys.com")
check_status("crsmongodb02.p01.eng.sjc01.qualys.com")
check_status("prom01.p01.eng.sjc01.qualys.com")
check_status("elsdatacmn02.p01.eng.sjc01.qualys.com")
# check_status("cmsdb01.p01.eng.sjc01.qualys.com")
check_status("kubeetcd01.p01.eng.sjc01.qualys.com")
check_status("masifgw01.p01.eng.sjc01.qualys.com")
check_status("masifgw02.p01.eng.sjc01.qualys.com")
check_status("qkafka01.p01.eng.sjc01.qualys.com")
check_status("qkafka02.p01.eng.sjc01.qualys.com")
check_status("kubenode01.p01.eng.sjc01.qualys.com")
check_status("kubenode02.p01.eng.sjc01.qualys.com")
check_status("qelsdataioc01.p13.eng.sjc01.qualys.com")
