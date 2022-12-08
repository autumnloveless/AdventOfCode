"""Advent of Code 2022 - Challenge 7 Part 1"""

from pprint import pp
from dataclasses import dataclass
from typing import List, Union, Optional, Dict

# Get Input
with open("inputs/day7.txt", 'r') as file:
    input = [line.strip() for line in file.readlines()]
input.pop(0)

@dataclass
class File:
    name: str
    size: int

@dataclass
class Directory:
    name: str
    files: Dict[str, Union[File,"Directory"]]
    parent_directory: Optional["Directory"]
    size: int

    def add_file(self, name, size):
        self.files[name] = (File(name, size))
        self.update_sizes()

    def update_sizes(self):
        self.size = self.get_dir_size(self)
        if self.parent_directory:
            self.parent_directory.update_sizes()

    def add_directory(self, name):
        self.files[name] = (Directory(name, {}, self, 0))

    def get_dir_size(self, directory: "Directory"):
        size = 0
        for file in directory.files.values():
            if isinstance(file, Directory):
                size += self.get_dir_size(file)
            else:
                size += file.size
        return size

class SystemScaler:

    file_system: Directory
    root_directory: Directory
    current_directory: Directory

    def __init__(self):
        self.file_system = Directory("/", {}, None, 0)
        self.root_directory = self.file_system
        self.current_directory = self.file_system

    def _process_command(self, command_raw: str):
        command = command_raw.strip("$ ")
        if not command.startswith("cd"):
            return
        self._change_directory(command.split(" ")[1])

    def _change_directory(self, path: str):
        if path == "/":
            self.current_directory = self.root_directory
        elif path == "..":
            self.current_directory = self.current_directory.parent_directory
        else:
            self.current_directory = self.current_directory.files[path]
    
    def _add_directory(self, raw_directory: str):
        directory = raw_directory.split(" ")[1]
        self.current_directory.add_directory(directory)

    def _add_file(self, raw_file: str):
        [size, name] = raw_file.split(" ")
        self.current_directory.add_file(name, int(size))

    def process_input(self, instructions: List[str]):
        for instruction in instructions:
            if instruction.startswith("$"):
                self._process_command(instruction)
            elif instruction.startswith("dir"):
                self._add_directory(instruction)
            else:
                self._add_file(instruction)

    def print_filesystem(self, directory: Directory=None, prefix="-"):
        directory = directory or self.root_directory
        for file in directory.files.values():
            if isinstance(file, Directory):
                print(prefix, "(dir)", file.name, file.size)
                self.print_filesystem(file, "  " + prefix)
            else :
               print(prefix, file.name, file.size)

    def get_small_dirs(self, max_size: int, directory: Directory=None) -> List[Directory]:
        directory = directory or self.root_directory
        small_dirs = []
        for file in directory.files.values():
            if not isinstance(file, Directory):
                continue
            if file.size <= max_size:
                small_dirs.append(file)
            small_dirs.extend(self.get_small_dirs(max_size, file))
        return small_dirs

system_scaler = SystemScaler()
system_scaler.process_input(input)


# system_scaler.print_filesystem()

small_dirs = system_scaler.get_small_dirs(100000)
total_size = 0
for dir in small_dirs:
    total_size += dir.size

print(total_size)
    

# calculate sums
