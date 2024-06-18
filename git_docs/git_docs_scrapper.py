import requests
from bs4 import BeautifulSoup
import jsonlines

# Function to extract content from a webpage
def extract_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad response status
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract title of the webpage from the first paragraph within sect1
        title = soup.find('div', class_='paragraph').get_text(separator=' ', strip=True)

        # Extract content from specific sections (assuming multiple divs with class 'sect1')
        sections = soup.find_all('div', class_='sect1')

        jsonl_entries = []
        for section in sections:
            # Extract section text from sectionbody
            sectionbody = section.find('div', class_='sectionbody')
            h2 = section.find('h2')
            
            if sectionbody:
                section_text = sectionbody.get_text(separator=' ', strip=True)
                if h2:
                    section_text = h2.get_text(separator=' ', strip=True) + " " + section_text
            else:
                section_text = ""

            # Check if dl tags are present
            dl_tags = section.find_all('dl')
            if dl_tags:
                for dl in dl_tags:
                    dt_tags = dl.find_all('dt')
                    dd_tags = dl.find_all('dd')

                    # Process dt and dd pairs
                    user_message_parts = []
                    assistant_messages = []

                    # Gather all dt tags until encountering a dd tag
                    for tag in dl.contents:
                        if tag.name == 'dt':
                            user_message_parts.append(tag.get_text(separator=' ', strip=True))
                        elif tag.name == 'dd':
                            dd_text = tag.get_text(separator=' ', strip=True)
                            if user_message_parts:
                                user_message = f"{title}  {'  '.join(user_message_parts)}"
                                data = {
                                    "messages": [
                                        {
                                            "role": "system",
                                            "content": "You are a helpful assistant."
                                        },
                                        {
                                            "role": "user",
                                            "content": user_message
                                        },
                                        {
                                            "role": "assistant",
                                            "content": dd_text
                                        }
                                    ]
                                }
                                jsonl_entries.append(data)
                                user_message_parts = []  # Reset user message parts
                            else:
                                # If there's no preceding dt tags, treat dd as standalone assistant message
                                data = {
                                    "messages": [
                                        {
                                            "role": "system",
                                            "content": "You are a helpful assistant."
                                        },
                                        {
                                            "role": "user",
                                            "content": title
                                        },
                                        {
                                            "role": "assistant",
                                            "content": dd_text
                                        }
                                    ]
                                }
                                jsonl_entries.append(data)

                    # If there are remaining user message parts after processing all dd tags
                    if user_message_parts:
                        user_message = f"{title}  {'  '.join(user_message_parts)}"
                        data = {
                            "messages": [
                                {
                                    "role": "system",
                                    "content": "You are a helpful assistant."
                                },
                                {
                                    "role": "user",
                                    "content": user_message
                                },
                                {
                                    "role": "assistant",
                                    "content": assistant_messages[-1]['content'] if assistant_messages else ""
                                }
                            ]
                        }
                        jsonl_entries.append(data)

            else:
                # If no dl tags, create a single entry for the section
                if section_text:
                    data = {
                        "messages": [
                            {
                                "role": "system",
                                "content": "You are a helpful assistant."
                            },
                            {
                                "role": "user",
                                "content": title
                            },
                            {
                                "role": "assistant",
                                "content": section_text
                            }
                        ]
                    }
                    jsonl_entries.append(data)

        return jsonl_entries

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# List of URLs to process
urls = ['https://www.git-scm.com/docs/git#_git_commands', 'https://www.git-scm.com/docs/git', 'https://www.git-scm.com/docs/git-config', 'https://www.git-scm.com/docs/git-help', 'https://www.git-scm.com/docs/git-bugreport', 'https://www.git-scm.com/docs/git-init', 'https://www.git-scm.com/docs/git-clone', 'https://www.git-scm.com/docs/git-add', 'https://www.git-scm.com/docs/git-status', 'https://www.git-scm.com/docs/git-diff', 'https://www.git-scm.com/docs/git-commit', 'https://www.git-scm.com/docs/git-notes', 'https://www.git-scm.com/docs/git-restore', 'https://www.git-scm.com/docs/git-reset', 'https://www.git-scm.com/docs/git-rm', 'https://www.git-scm.com/docs/git-mv', 'https://www.git-scm.com/docs/git-branch', 'https://www.git-scm.com/docs/git-checkout', 'https://www.git-scm.com/docs/git-switch', 'https://www.git-scm.com/docs/git-merge', 'https://www.git-scm.com/docs/git-mergetool', 'https://www.git-scm.com/docs/git-log', 'https://www.git-scm.com/docs/git-stash', 'https://www.git-scm.com/docs/git-tag', 'https://www.git-scm.com/docs/git-worktree', 'https://www.git-scm.com/docs/git-fetch', 'https://www.git-scm.com/docs/git-pull', 'https://www.git-scm.com/docs/git-push', 'https://www.git-scm.com/docs/git-remote', 'https://www.git-scm.com/docs/git-submodule', 'https://www.git-scm.com/docs/git-show', 'https://www.git-scm.com/docs/git-log', 'https://www.git-scm.com/docs/git-diff', 'https://www.git-scm.com/docs/git-difftool', 'https://www.git-scm.com/docs/git-range-diff', 'https://www.git-scm.com/docs/git-shortlog', 'https://www.git-scm.com/docs/git-describe', 'https://www.git-scm.com/docs/git-apply', 'https://www.git-scm.com/docs/git-cherry-pick', 'https://www.git-scm.com/docs/git-diff', 'https://www.git-scm.com/docs/git-rebase', 'https://www.git-scm.com/docs/git-revert', 'https://www.git-scm.com/docs/git-bisect', 'https://www.git-scm.com/docs/git-blame', 'https://www.git-scm.com/docs/git-grep', 'https://www.git-scm.com/docs/gitattributes', 'https://www.git-scm.com/docs/gitcli', 'https://www.git-scm.com/docs/giteveryday', 'https://www.git-scm.com/docs/gitfaq', 'https://www.git-scm.com/docs/gitglossary', 'https://www.git-scm.com/docs/githooks', 'https://www.git-scm.com/docs/gitignore', 'https://www.git-scm.com/docs/gitmodules', 'https://www.git-scm.com/docs/gitrevisions', 'https://www.git-scm.com/docs/gitsubmodules', 'https://www.git-scm.com/docs/gittutorial', 'https://www.git-scm.com/docs/gitworkflows', 'https://www.git-scm.com/docs/git#_guides', 'https://www.git-scm.com/docs/git-am', 'https://www.git-scm.com/docs/git-apply', 'https://www.git-scm.com/docs/git-format-patch', 'https://www.git-scm.com/docs/git-send-email', 'https://www.git-scm.com/docs/git-request-pull', 'https://www.git-scm.com/docs/git-svn', 'https://www.git-scm.com/docs/git-fast-import', 'https://www.git-scm.com/docs/git-clean', 'https://www.git-scm.com/docs/git-gc', 'https://www.git-scm.com/docs/git-fsck', 'https://www.git-scm.com/docs/git-reflog', 'https://www.git-scm.com/docs/git-filter-branch', 'https://www.git-scm.com/docs/git-instaweb', 'https://www.git-scm.com/docs/git-archive', 'https://www.git-scm.com/docs/git-bundle', 'https://www.git-scm.com/docs/git-daemon', 'https://www.git-scm.com/docs/git-update-server-info', 'https://www.git-scm.com/docs/git-cat-file', 'https://www.git-scm.com/docs/git-check-ignore', 'https://www.git-scm.com/docs/git-checkout-index', 'https://www.git-scm.com/docs/git-commit-tree', 'https://www.git-scm.com/docs/git-count-objects', 'https://www.git-scm.com/docs/git-diff-index', 'https://www.git-scm.com/docs/git-for-each-ref', 'https://www.git-scm.com/docs/git-hash-object', 'https://www.git-scm.com/docs/git-ls-files', 'https://www.git-scm.com/docs/git-ls-tree', 'https://www.git-scm.com/docs/git-merge-base', 'https://www.git-scm.com/docs/git-read-tree', 'https://www.git-scm.com/docs/git-rev-list', 'https://www.git-scm.com/docs/git-rev-parse', 'https://www.git-scm.com/docs/git-show-ref', 'https://www.git-scm.com/docs/git-symbolic-ref', 'https://www.git-scm.com/docs/git-update-index', 'https://www.git-scm.com/docs/git-update-ref', 'https://www.git-scm.com/docs/git-verify-pack', 'https://www.git-scm.com/docs/git-write-tree']

# Output file path
output_file = "train.jsonl"

# Process each URL and write to JSONL file
with jsonlines.open(output_file, mode='w') as writer:
    for url in urls:
        content_data = extract_content(url)
        if content_data:
            for entry in content_data:
                writer.write(entry)
            print(f"Processed {url} successfully.")

print(f"Output saved to {output_file}")
