import re

class LogParser:
    LOG_PATTERN = re.compile(r'\[(?P<time>.*?)\]\s+(?P<level>\w+):\s+(?P<msg>.*)')

    def __init__(self, path):
        self.path = path

    def __iter__(self):
        with open(self.path) as f:
            for line in f:
                m = self.LOG_PATTERN.match(line)
                if m:
                    yield m.groupdict()

    def count_by_level(self):
        counts = {}
        for entry in self:
            lvl = entry["level"]
            counts[lvl] = counts.get(lvl, 0) + 1
        return counts
