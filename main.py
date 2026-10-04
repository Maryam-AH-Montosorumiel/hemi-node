import os
import subprocess
import urllib.request
import tarfile

def download_and_run_hemi():
    archive = "hemi.tar.gz"
    
    # رابط مباشر ومقسم برمجياً لضمان عدم القص أو التداخل من المتصفح
    host = "https://github.com"
    path = "/hemilabs/heminetwork/releases/download/v0.4.3/heminetwork_v0.4.3_linux_amd64.tar.gz"
    full_url = host + path
    
    print("🤖 Automated Miner -> Downloading Hemi Node...")
    try:
        # استخدام مكتبة النظام الرسمية للتحميل لضمان الاستقرار
        urllib.request.urlretrieve(full_url, archive)
    except Exception as e:
        print(f"❌ Download failed: {str(e)}")
        return
        
    print("📦 Automated Miner -> Extracting official node files...")
    with tarfile.open(archive, "r:gz") as tar:
        tar.extractall()
        
    # الانتقال إلى المجلد المستخرج وتشغيل العقدة
    os.chdir("heminetwork_v0.4.3_linux_amd64")
    
    private_key = os.environ.get("HEMI_PRIVATE_KEY")
    if not private_key:
        print("❌ Error: HEMI_PRIVATE_KEY environment variable is missing!")
        return

    print("🚀 Booting Hemi PoP Miner on Cloud Network...")
    cmd = "./popmd"
    
    env = os.environ.copy()
    env["POPMD_PRIVATE_KEY"] = private_key
    env["POPMD_STATIC_PEERS"] = "/dns4/popm.testnet.hemi.network/tcp/443/wss"
    
    process = subprocess.Popen(cmd, shell=True, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in process.stdout:
        print(line, end="")

if __name__ == "__main__":
    download_and_run_hemi()
