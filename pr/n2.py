import collections

def analyze_word_frequency():
    try:
        with open("log.txt", "r", encoding="utf-8") as source_file:
            raw_content = source_file.read()
            word_list = raw_content.lower().split()
        
        word_frequency_map = collections.Counter(word_list)
        most_popular_words = word_frequency_map.most_common(10)
        
        with open("word_stats.txt", "w", encoding="utf-8") as stats_file:
            for word, occurrence_count in most_popular_words:
                stats_file.write(f"{word}: {occurrence_count}\n")
                
    except FileNotFoundError:
        print("Помилка: вхідний файл не знайдено.")

analyze_word_frequency()