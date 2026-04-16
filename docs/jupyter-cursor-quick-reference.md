# Jupyter in Cursor — quick reference

Cursor’s notebook UI matches **VS Code + the Jupyter extension**. Defaults below follow the [official VS Code Jupyter docs](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) (on macOS, **Ctrl**+**Enter** is still **Ctrl**, not Cmd).

**Note:** In VS Code/Cursor, **Shift**+**Enter** and **Alt**+**Enter** insert a **new** cell below after running. That differs from classic Jupyter Lab, where **Shift**+**Enter** usually moves to the next existing cell.

## Run cells

| Action | Shortcut | Command Palette (search) |
|--------|----------|---------------------------|
| Run cell, stay on this cell | **Ctrl**+**Enter** | `Notebook: Execute Cell` |
| Run cell, insert new cell below, focus **new** cell | **Shift**+**Enter** | (same behavior; see `Notebook: Execute Cell and Insert Below` variants in Keyboard Shortcuts) |
| Run cell, insert new cell below, focus **stays** on current | **Alt**+**Enter** (**Option**+**Enter** on Mac) | related execute/insert commands |
| Run all / above / below | Toolbar **Run All** menu | `Notebook: Run All`, `Run All Above`, `Run All Below` |

## Command mode (vim-style)

Press **Esc** when a cell is focused to leave **edit mode** (green outline) and enter **command mode** (blue bar on the left). **Enter** opens the cell for editing again.

| Key | Action |
|-----|--------|
| **A** / **B** | Insert cell **above** / **below** |
| **J** / **K** or **↑** / **↓** | Select previous / next cell |
| **M** / **Y** | Turn cell into **Markdown** / **code** |
| **D** **D** (double) | **Delete** selected cell(s) |
| **Z** | **Undo** last notebook edit (e.g. accidental delete) |
| **L** | Line numbers (cell); **Shift**+**L** whole notebook |

## Kernel & outputs

| Goal | How |
|------|-----|
| Choose kernel | Top-right kernel picker, or `Notebook: Select Notebook Kernel` |
| Interrupt | Toolbar stop, or `Jupyter: Interrupt Kernel` |
| Restart | `Jupyter: Restart Kernel` |
| Clear outputs | `Notebook: Clear All Outputs` |
| Variables | Toolbar **Variables** after running code (Variable Explorer / Data Viewer) |

## Editor conveniences

| Goal | Shortcut / command |
|------|-------------------|
| Command Palette | **Shift**+**Cmd**+**P** |
| Search in notebook | **Cmd**+**F** — use the **filter** (funnel) to include rendered Markdown, outputs, etc. |
| Outline / TOC | Side bar **Outline** (see `notebook.outline.*` settings for code cells in outline) |
| Rebind keys | **Cmd**+**K** **Cmd**+**S** → search `notebook` or `jupyter` |

## Trust & Python

- **Workspace Trust** can block execution in untrusted folders; see Cursor/VS Code workspace trust settings if cells won’t run.
- Pick an interpreter/kernel that matches your project (e.g. `.venv`) via the kernel / Python selector.
