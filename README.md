Instalação:

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv python install 3.11
uv sync

Rode com: 

uv run python -m app.main