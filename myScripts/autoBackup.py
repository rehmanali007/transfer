import os
import pexpect
import shutil
import subprocess


home = "/home/virchual"
backup_dir = f"{home}/.backups"
if not os.path.exists(backup_dir):
    os.mkdir(backup_dir)

target_files = {
    "i3config": f"{home}/.config/i3/config",
    "sudoers": "/etc/sudoers.d/sudoers.local",
    "bash_aliases": f"{home}/.bash_aliases",
    "bashrc": f"{home}/.bashrc",
}


# ------------------------------------


def cron_backup():
    out = subprocess.getoutput("crontab -l")
    crontab_file = open("crontab", "w")
    crontab_file.write(out)
    crontab_file.close()


def sudoers_backup():
    child = pexpect.spawn('su - root')
    child.expect('Password:')
    child.sendline('universe07')
    child.expect('root')
    child.sendline(
        f'cp /etc/sudoers.d/sudoers.local {backup_dir}/sudoers.local')
    print('Done!')

# for f in target_files.values():
#     shutil.copy(f, backup_dir)


sudoers_backup()
