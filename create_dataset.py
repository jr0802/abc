import os
import urllib.request
import zipfile

def download_ag_news():
    url = "https://drive.google.com/uc?export=download&id=0Bz8a_Dbh9QhbUDNpeUdjb0wxRms"
    data_dir = os.path.join(os.path.dirname(__file__), "data", "ag_news")
    os.makedirs(data_dir, exist_ok=True)
    
    zip_path = os.path.join(data_dir, "ag_news_csv.zip")
    
    print("正在下载AG_NEWS数据集...")
    try:
        urllib.request.urlretrieve(url, zip_path)
        print("下载完成，正在解压...")
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(data_dir)
        
        os.remove(zip_path)
        print("数据集准备完成！")
        
        files = os.listdir(data_dir)
        print(f"数据目录内容: {files}")
        
    except Exception as e:
        print(f"下载失败: {e}")
        print("将使用内置的示例数据...")
        create_sample_data(data_dir)

def create_sample_data(data_dir):
    train_data = [
        "1,Fed official says weak data caused by weather, should not slow taper",
        "1,Sri Lankan president sacks cricket board after World Cup debacle",
        "1,Oil prices fall on OPEC output increase expectations",
        "1,Microsoft releases new Windows 10 update with improved security",
        "2,US stocks rise on positive economic data",
        "2,New smartphone model breaks sales records",
        "2,European markets close higher on trade optimism",
        "2,Apple announces new MacBook Pro with M3 chip",
        "3,Soccer team wins championship after dramatic final",
        "3,Tennis star advances to Grand Slam final",
        "3,Basketball player sets new scoring record",
        "3,Olympic committee approves new sports for 2028 Games",
        "4,Scientists discover new planet in habitable zone",
        "4,AI breakthrough improves natural language processing",
        "4,SpaceX launches new batch of Starlink satellites",
        "4,Medical researchers develop promising cancer treatment",
    ]
    
    test_data = [
        "1,Fed maintains interest rates amid economic uncertainty",
        "1,Government announces new climate policy",
        "1,International summit addresses global trade issues",
        "1,New healthcare bill passes in parliament",
        "2,Technology company reports record quarterly earnings",
        "2,Cryptocurrency prices surge on institutional adoption",
        "2,Retail sales increase during holiday season",
        "2,Central bank announces monetary policy changes",
        "3,Rugby team qualifies for international tournament",
        "3,Golf tournament attracts top players worldwide",
        "3,Track and field athletes break national records",
        "3,Volleyball team wins national championship",
        "4,Renewable energy technology achieves major milestone",
        "4,Quantum computing research makes progress",
        "4,Biotech startup secures funding for drug development",
        "4,5G network expansion continues across country",
    ]
    
    with open(os.path.join(data_dir, "train.csv"), 'w', encoding='utf-8') as f:
        for line in train_data:
            f.write(line + "\n")
    
    with open(os.path.join(data_dir, "test.csv"), 'w', encoding='utf-8') as f:
        for line in test_data:
            f.write(line + "\n")
    
    print("示例数据已创建！")

if __name__ == "__main__":
    download_ag_news()