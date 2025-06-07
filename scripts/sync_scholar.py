#!/usr/bin/env python3
"""Sync publications from Google Scholar to _publications/"""
import argparse
import os
import re
import html
from datetime import datetime

try:
    from scholarly import scholarly
except ImportError:
    raise SystemExit("The 'scholarly' package is required. Install with pip install scholarly")

def slugify(title: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", title.lower()).strip('-')
    return slug

def html_escape(text: str) -> str:
    return html.escape(text or "")


def format_citation(pub):
    bib = pub.get('bib', {})
    authors = bib.get('author', '')
    title = bib.get('title', '')
    venue = bib.get('venue', '')
    year = bib.get('pub_year', '')
    citation = f"{authors} \"{title}.\" {venue}, {year}."
    return citation


def create_markdown(pub, outdir):
    bib = pub.get('bib', {})
    title = bib.get('title', 'No title')
    venue = bib.get('venue', '')
    year = bib.get('pub_year', '1900')
    date = f"{year}-01-01"
    slug = slugify(title)
    filename = f"{date}-{slug}.md"
    permalink = f"/publication/{date}-{slug}"
    citation = format_citation(pub)
    md = []
    md.append('---')
    md.append(f"title: \"{html_escape(title)}\"")
    md.append("collection: publications")
    md.append(f"permalink: {permalink}")
    md.append(f"date: {date}")
    if venue:
        md.append(f"venue: '{html_escape(venue)}'")
    md.append(f"citation: '{html_escape(citation)}'")
    md.append('---')
    query = '+'.join(slug.split('-'))
    md.append(f"Use [Google Scholar](https://scholar.google.com/scholar?q={query}){{:target=\"_blank\"}} for full citation")
    with open(os.path.join(outdir, filename), 'w', encoding='utf-8') as f:
        f.write("\n".join(md))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--author-id', required=True, help='Google Scholar user ID')
    parser.add_argument('--output', default='_publications', help='Output directory')
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    author = scholarly.search_author_id(args.author_id)
    author = scholarly.fill(author, sections=['publications'])
    for pub in author.get('publications', []):
        pub = scholarly.fill(pub)
        create_markdown(pub, args.output)

if __name__ == '__main__':
    main()
