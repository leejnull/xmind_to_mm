#!/usr/bin/python3
import os
import sys
from typing import List
from xmindparser import xmind_to_dict

class Node:
    title: str
    note: str
    topics: List[any]
    
    def __init__(self, title: str, note: str, topics: List[any]) -> None:
        if title:
            if '<' in title:
                self.title = title.replace('<', '小于')
            elif '"' in title:
                self.title = title.replace('"', '\'')
            else:
                self.title = title
        else:
            self.title = ''
        self.note = note
        self.topics = topics
        
    def __str__(self) -> str:
        return '{0}-{1}-{2}'.format(self.title, self.note, self.topics)

def recursionRead(d: dict) -> None:
    title = d['title']
    note = None
    if 'note' in d:
        note = d['note']
    if 'topics' not in d:
        node = Node(title, note, None)
        return node
    topics = d['topics']
    topic_list = []
    for topic in topics:
        node = recursionRead(topic)
        topic_list.append(node)
    node = Node(title, note, topic_list)
    return node

def recursionWrite(node: Node) -> str:
    prefix = '<node TEXT="{0}" FOLDED="true">'.format(node.title)
    suffix = '</node>'
    if not node.topics or len(node.topics) == 0:
        return '\n'.join([prefix, suffix])
    else:
        topic_str_list = []
        for subNode in node.topics:
            topic_str_list.append(recursionWrite(subNode))
        topic_str = '\n'.join(topic_str_list)
        return '\n'.join([prefix, topic_str, suffix])

def main():
    if len(sys.argv) < 2:
        print('''
              脚本执行命令：python3 xmind_to_mm.py 文件路径\n
              eg: python3 xmind_to_mm.py 1.8测试用例.xmind
              ''')
        return
    path = sys.argv[1]
    d = xmind_to_dict(path)[0]
    if 'topic' in d:
        res = recursionRead(d['topic'])
    else:
        res = recursionRead(d)
    basename = os.path.basename(path)
    write_path = '{0}.mm'.format('.'.join(basename.split('.')[:-1]))
    with open(write_path, 'w') as f:
        f.write('<?xml version="1.0" ?>')
        f.write('<map version="0.8.1">')
        f.write(recursionWrite(res))
        f.write('</map>')

if __name__ == '__main__':
    main()
