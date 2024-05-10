import subprocess

def upgrade_dependencies():
    try:
        # Run pip list to get a list of installed packages
        result = subprocess.run(['pip', 'list', '--format=freeze'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        installed_packages = result.stdout.split('\n')

        # Filter out Jupyter Lab related packages and upgrade the remaining ones
        packages_to_upgrade = [pkg.split('==')[0] for pkg in installed_packages if 'jupyter' not in pkg.lower()]
        
        if len(packages_to_upgrade) == 0:
            print("No packages found to upgrade.")
            return
        
        # Upgrade packages
        print("Upgrading packages...")
        for package in packages_to_upgrade:
            subprocess.run(['pip', 'install', '--upgrade', package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        print("All packages upgraded successfully.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    upgrade_dependencies()
