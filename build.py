# LightBot build
import subprocess
from os import system, path as osp, mkdir, getcwd

from requests import get
import yaml


def checkConfig():
    if osp.exists("PythonCore/config/version.yml"):
        with open("PythonCore/config/version.yml", "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            if data['version'] == buildConfig['version']:
                del f
            else:
                if not osp.exists("PythonCore/config"):
                    mkdir("PythonCore/config")
                with open("PythonCore/config/buildconfig.yml", "w") as k:
                    k.write(get("https://github.com/Undef1nedT1am/LightBot/raw/master/config/buildconfig.yml").text)
                    del k
    else:
        with open("PythonCore/config/version.yml", "w") as f:
            f.write(get("https://github.com/Undef1nedT1am/LightBot/raw/master/version.yml").text)
            checkConfig()


def readBuildConfig():
    with open('PythonCore/config/buildconfig.yml', 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data


def check_pip_package():
    try:
        print(f'{getcwd()}{buildConfig["python"]["pythonPath"]}',)
        output = subprocess.run([f'{buildConfig["python"]["pythonPath"]}', '-m', 'pip', 'list'], check=True,
                                stdout=subprocess.PIPE, text=True)
        packages = output.stdout.splitlines()
        with open('requirements.txt', 'r') as f:
            packs = f.readlines()
            del f
        for package_name in packs:
            if package_name not in packages:
                print("Didn't install " + package_name)
                system(f'{buildConfig["python"]["pythonPath"]} -m pip install {package_name}')

    except subprocess.CalledProcessError:
        return False


def build():
    if bool(buildConfig['enablePython']):

        arg_a = buildConfig['python']
        args = [
            "--onefile" if bool(arg_a['onefile']) else "--standalone"
                                                       "--lto=yes" if bool(arg_a['lto']) else "--lto=no"
                                                                                              "--remove-output" if bool(
                arg_a["removeOutput"]) else ""
                                            "--output-dir=" + arg_a['outputDir']
        ]
        command = f'{buildConfig["python"]["pythonPath"]} '
        for arg in args:
            command += arg + " "
        print("Build command:\n" + command)
        system(command)


if __name__ == "__main__":
    buildConfig = readBuildConfig()
    print("Checking version...")
    checkConfig()
    check_pip_package()
    print("ok start build")
