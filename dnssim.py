import re

def extract_domains_from_log_file(log_file_path): "/data/dns/2022-08-13_dns.09:00:00-10:00:00.log"
    """
    Extracts the domains from a log file.

    Args:
        log_file_path (str): The path to the log file.

    Returns:
        set: A set of domains found in the log file.
    """
    domains = set()
    with open(log_file_path, 'r') as f:
        for line in f:
            match = re.search(r'http[s]?://([\w.-]+)', line)
            if match:
                domain = match.group(1)
                domains.add(domain)
    return domains

def tokenize_into_trigrams(domain):
    """
    Tokenizes a domain into trigrams.

    Args:
        domain (str): The domain to tokenize.

    Returns:
        set: A set of trigrams found in the domain.
    """
    trigrams = set()
    for i in range(len(domain) - 2):
        trigrams.add(domain[i:i+3])
    return trigrams

def calculate_jaccard_similarity(set1, set2):
    """
    Calculates the Jaccard similarity between two sets.

    Args:
        set1 (set): The first set.
        set2 (set): The second set.

    Returns:
        float: The Jaccard similarity score.
    """
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

# Example usage
log_file_path = 'example.log'
domains = extract_domains_from_log_file(log_file_path)

# Tokenize domains into trigrams
domain_trigrams = {}
for domain in domains:
    trigrams = tokenize_into_trigrams(domain)
    domain_trigrams[domain] = trigrams

# Calculate Jaccard similarity between domains
for domain1 in domains:
    for domain2 in domains:
        if domain1 != domain2:
            jaccard_similarity = calculate_jaccard_similarity(domain_trigrams[domain1], domain_trigrams[domain2])
            print(f"Jaccard similarity between {domain1} and {domain2}: {jaccard_similarity}")
