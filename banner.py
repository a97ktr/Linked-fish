# banner.py
import random
import pyfiglet
from rich.console import Console
from rich.progress import track
import time

console = Console()

BANNER_STYLES = [
    "slant", "graffiti", "doom", "larry3d", "isometric1",
    "cybermedium", "alligator2", "rectangles", "starwars", 'block', 'bubble'
]

def generate_banner(tool_name):
    style = random.choice(BANNER_STYLES)
    banner = pyfiglet.figlet_format(tool_name, font=style)
    console.print(f"[bold green]{banner}[/bold green]")

def loading_screen():
    console.print("[cyan]Scraping LinkedIn Profiles...[/cyan]")
    for _ in track(range(100), description="[bold magenta]Starting Tool [/bold magenta]"):
        time.sleep(0.04)
    console.print("[bold green]READY TO DIVE![/bold green]")

def startup_screen(tool_name, version="1.0.0", author="KATROU"):
    console.clear()
    generate_banner(tool_name)
    console.print(f"[bold yellow]Version: {version}[/bold yellow]")
    console.print(f"[bold blue]Author: {author}[/bold blue]")
    console.print("[bold red]DISCLAIMER: Use responsibly! Educational purposes only.[/bold red]\n")
    loading_screen()
