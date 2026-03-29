from pathlib import Path

from pathlib import Path

prompt_file = Path(__file__).parent.parent / "prompts" / "prompt_1.txt"
results_folder = Path(__file__).parent.parent / "results"
results_folder.mkdir(exist_ok=True)
output_file = results_folder / "output_1.txt"

# Read prompt
with prompt_file.open() as f:
    prompt = f.read()

# Example processing
output = f"Processed Prompt Output:\n{prompt.upper()}"

# Save result
with output_file.open("w") as f:
    f.write(output)

print("Prompt processed and output saved!") # one level up from scripts → prompts
results_folder = Path("../results")
results_folder.mkdir(exist_ok=True)
output_file = results_folder / "output_1.txt"

# Read prompt
with prompt_file.open() as f:
    prompt = f.read()

# Example processing
output = f"Processed Prompt Output:\n{prompt.upper()}"

# Save result
with output_file.open("w") as f:
    f.write(output)

print("Prompt processed and output saved!")