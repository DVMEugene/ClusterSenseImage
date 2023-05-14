import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('keywords.db')
c = conn.cursor()

# Create SERP_TABLE
c.execute('''
    CREATE TABLE IF NOT EXISTS keywords_serps (
        requestTimestamp TEXT,
        searchTerms TEXT,
        gl TEXT,
        hl TEXT,
        totalResults INTEGER,
        link TEXT,
        displayLink TEXT,
        main_domain TEXT,
        position INTEGER,
        snippet TEXT,
        snipped_language TEXT,
        snippet_matchScore_order INTEGER,
        snippet_matchScore_token INTEGER,
        title TEXT,
        title_matchScore_order INTEGER,
        title_matchScore_token INTEGER
    )
''')

# Create CLUSTER_TABLE
c.execute('''
    CREATE TABLE IF NOT EXISTS keyword_clusters (
        requestTimestamp TEXT,
        cluster INTEGER,
        searchTerms TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
