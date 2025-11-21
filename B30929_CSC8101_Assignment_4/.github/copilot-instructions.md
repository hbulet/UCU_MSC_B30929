<!-- Copilot instructions for AI coding agents working on this repo -->
# Copilot Instructions — TKinter Assignment App

Purpose
- Help an AI coding agent quickly understand, run, and safely modify this small Tkinter-based GUI project.

Quick run commands
- Run the main GUI (primary app):
  - `python TKinter/GUIControls.py`
- Run the loan calculator sample window:
  - `python TKinter/LoanCalculator.py`
- These are simple single-file entry points using the system `tkinter` library; no third-party packages required.

Big-picture architecture
- Small desktop GUI app (no web/backend). Main components:
  - `TKinter/MyFrame.py`: primary application frame, menu, and launcher for the feedback dialog. This is the canonical entry implementation.
  - `TKinter/FeedBackDlg.py`: modal feedback dialog used by `MyFrame` (dialog is invoked via `FeedBackDlg(self.parent)` and `dialog.show()` — keep modal semantics).
  - `TKinter/LoanCalculatorMyFrame.py` + `TKinter/LoanCalculator.py`: a second, self-contained sample window that implements a simple loan calculator UI. Use this for isolated UI experiments.
  - `TKinter/GUIControls.py`: alternate entrypoint that constructs `MyFrame` with a larger window.

Project-specific patterns and conventions
- Geometry & widgets:
  - Uses `place()` geometry manager (absolute coordinates). Avoid converting to `grid`/`pack` unless you update all coordinates consistently.
  - Uses `ttk.Style` with custom style names like `MainButton.TButton` and `Exit.TButton` — preserve style names when modifying buttons.
- Readonly entries:
  - Some `Entry` widgets are set `state='readonly'` and temporarily toggled to `normal` before `delete()`/`insert()` and then set back to `readonly`. Keep that pattern when updating computed fields (see `LoanCalculatorMyFrame.calcButtonClick`).
- Exit handling:
  - Exit logic calls `sys.exit()` after `self.parent.destroy()` in several places. If you change process termination behavior, ensure both window destruction and process exit semantics are preserved.
- Dialogs:
  - `FeedBackDlg` is modal: the code expects `dialog.show()` to call `wait_window()` or equivalent. Preserve that behavior if refactoring.

Code-level notes and examples
- Calculations: `LoanCalculatorMyFrame.calcButtonClick` computes monthly payment using floats and inserts formatted strings into readonly `Entry`s. Example: keep `format(..., "0.2f")` for consistent 2-decimal output.
- Names & imports:
  - Many modules use local imports like `from LoanCalculatorMyFrame import MyFrame` and `from MyFrame import MyFrame`. Use relative imports only if you update the module layout.

Developer workflows
- No tests/build system present. To run or debug:
  - Run the entry module with Python in the project root: `python TKinter/GUIControls.py` or `python TKinter/LoanCalculator.py`.
  - On Windows PowerShell example: `& C:/Python313/python.exe "TKinter/LoanCalculator.py"` (adapt path to the user's Python).
- Quick static checks:
  - Linting/formatting isn't configured. If adding formatting, target only changed files to avoid large diffs.

When changing UI/behavior
- Keep UIs backward-compatible: maintain style names, the `place()` coordinates, and dialog modality.
- If modifying `FeedBackDlg` API, update all callers (`MyFrame.btnLaunchFeedback` and other entry points).

When committing changes
- Keep changes small and focused (this is a teaching/assignment repo). Avoid sweeping refactors that change layout managers or remove `sys.exit()` behavior without explicit tests.

Where to look first when asked to modify something
- Change menu or dialog behavior: `TKinter/MyFrame.py`.
- Change loan calculation or UI formatting: `TKinter/LoanCalculatorMyFrame.py`.
- Add or test another window: `TKinter/LoanCalculator.py` and `TKinter/GUIControls.py`.

If something is unclear
- Ask about the intended UI behavior (closing behavior, modal vs non-modal, layout changes). Mention which entrypoint you will run to verify locally.

End of instructions — ask me for clarification or areas to expand.
