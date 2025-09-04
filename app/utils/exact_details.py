import re
from datetime import datetime

def extract_tasks(transcript: str):
    tasks = []
    lines = [l.strip() for l in transcript.splitlines() if l.strip()]
    idc = 1
    # look for lines like "Name: action..." or sentences with "need", "will", "can you", "please", "assign"
    for i, line in enumerate(lines):
        m = re.match(r'^(?P<who>[A-Z][a-z]+):\s*(?P<rest>.+)$', line)
        if m:
            who = m.group('who')
            rest = m.group('rest')
            # heuristics for "action-looking" sentences
            if re.search(r'\b(need|need to|must|please|will|will need|can you|assign|fix|investigate|provide|send|review|run|allocate)\b', rest, re.I):
                task = {
                    "id": idc,
                    "title": rest.split('.')[0][:80],
                    "assignee": who,
                    "priority": None,
                    "due_date": None,
                    "description": rest,
                    "notes": ""
                }
                tasks.append(task)
                idc += 1
    return tasks