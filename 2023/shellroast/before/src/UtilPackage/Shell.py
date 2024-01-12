
from colorama import Fore as f
from dataclasses import dataclass


@dataclass
class Command:
	CMD: str
	argv: list[str]
	def __repr__(self): return f'<cmd: {self.CMD}, args: {self.getArgStr()} arglen: {len(self.argv)}>' 
	def getArgStr(self): return ' ,'.join([f'{i}\n' for i in self.argv])
	def __str__(self): return self.__repr__()


class Shell:
	""" A basic shell out of the box. """
	
	def shellInput(self, Tool: str = None) -> Command | bool:
		""" Gets User input then returns a parsed command. """
		if Tool:
			re_val = self.parseCmd(input(f"  {f.YELLOW}[*][{Tool}] {f.CYAN}-> {f.WHITE}"))
		else:
			re_val = self.parseCmd(input(f"  {f.YELLOW}[*] {f.CYAN}-> {f.WHITE}"))
		return re_val if re_val else False
	
	def parseCmd(self, cmd: str) -> Command | bool:
		""" Parses a command and returns the command and its args. """
		if not cmd:
			return False

		else:
			return (
				Command(
					cmd.split(' ')[0].strip().upper(),
					[i.strip() for i in cmd.split(' ')[1:]],
				)
				if len(cmd.split(' ')) > 1
				else Command(cmd.split(' ')[0].strip().upper(), [])
			)



























