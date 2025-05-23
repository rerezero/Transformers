from subprocess import run, PIPE
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI  = ROOT / "src" / "cli.py"
SAMPLE = "Монгол Улсын нийслэл Улаанбаатар хот хүн ам, эдийн засгийн хувьд ..."

def test_runs_ok():
    proc = run(["python", CLI, "-i", "-"],
               input=SAMPLE.encode(),
               stdout=PIPE, stderr=PIPE, check=True)
    assert "SUMMARY" in proc.stdout.decode()

