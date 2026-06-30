import os
import random

world_topics = [
    "government", "policy", "president", "election", "parliament",
    "congress", "bill", "law", "reform", "diplomacy", "treaty",
    "summit", "international", "peace", "war", "conflict",
    "crisis", "aid", "humanitarian", "climate", "environment",
    "global warming", "pollution", "healthcare", "pandemic",
    "vaccine", "education", "immigration", "refugee", "economy",
    "trade", "terrorism", "security", "natural disaster", "protest"
]

sports_topics = [
    "football", "soccer", "basketball", "tennis", "rugby",
    "cricket", "golf", "Olympics", "World Cup", "championship",
    "league", "team", "player", "match", "score", "win", "loss",
    "goal", "record", "champion", "victory", "training", "fan"
]

business_topics = [
    "stock", "market", "company", "investment", "earnings",
    "profit", "revenue", "sales", "consumer", "product",
    "merger", "acquisition", "bank", "finance", "technology",
    "retail", "e-commerce", "energy", "real estate", "startup"
]

tech_topics = [
    "technology", "AI", "artificial intelligence", "machine learning",
    "computer", "software", "smartphone", "internet", "cloud",
    "data", "security", "cybersecurity", "social media", "5G",
    "network", "chip", "processor", "quantum computing", "blockchain"
]

templates = [
    "{topic} {verb} {detail}",
    "{topic} {verb} as {detail}",
    "New {topic} {verb} {detail}",
    "{topic} {verb} in {location}",
    "{topic} {verb} worldwide",
    "{topic} experts {verb} {detail}",
    "{detail} {verb} over {topic}",
    "{topic} policy {verb} {detail}",
    "{topic} {verb} this week",
    "{topic} {verb} latest"
]

verbs = [
    "announces", "reports", "launches", "reveals", "releases",
    "introduces", "implements", "approves", "passes", "says",
    "states", "declares", "warns", "predicts", "continues",
    "expands", "improves", "develops", "faces", "deals with",
    "addresses", "tackles", "breaks", "sets", "achieves",
    "rises", "falls", "increases", "decreases", "grows"
]

details = [
    "with new features", "for the first time", "after months of work",
    "in a major development", "due to recent events",
    "according to officials", "as expected", "surprisingly",
    "in record time", "with significant impact",
    "to address concerns", "following recent trends",
    "in response to demand", "with positive results",
    "despite challenges", "in a landmark decision",
    "as part of ongoing efforts", "to meet growing needs",
    "in an unexpected move", "following negotiations"
]

locations = [
    "the US", "Europe", "Asia", "China", "India", "Japan",
    "Germany", "France", "the UK", "Brazil", "Russia",
    "Australia", "Canada", "the Middle East", "Africa"
]

def generate_news(category):
    if category == 0:
        topic = random.choice(world_topics)
    elif category == 1:
        topic = random.choice(sports_topics)
    elif category == 2:
        topic = random.choice(business_topics)
    else:
        topic = random.choice(tech_topics)
    
    template = random.choice(templates)
    verb = random.choice(verbs)
    detail = random.choice(details)
    location = random.choice(locations)
    
    return template.format(topic=topic, verb=verb, detail=detail, location=location)

def generate_dataset():
    data_dir = os.path.join(os.path.dirname(__file__), "data", "ag_news")
    os.makedirs(data_dir, exist_ok=True)
    
    train_samples_per_class = 10000
    test_samples_per_class = 500
    
    with open(os.path.join(data_dir, "train.csv"), 'w', encoding='utf-8') as train_file:
        for category in range(4):
            for _ in range(train_samples_per_class):
                news = generate_news(category)
                train_file.write(f"{category+1},{news}\n")
    
    with open(os.path.join(data_dir, "test.csv"), 'w', encoding='utf-8') as test_file:
        for category in range(4):
            for _ in range(test_samples_per_class):
                news = generate_news(category)
                test_file.write(f"{category+1},{news}\n")
    
    print("数据集生成完成！")
    print(f"训练集: {train_samples_per_class * 4} 条")
    print(f"测试集: {test_samples_per_class * 4} 条")

if __name__ == "__main__":
    generate_dataset()