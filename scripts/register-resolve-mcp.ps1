$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$pythonPath = Join-Path $projectRoot '.venv-resolve/Scripts/python.exe'
$serverPath = Join-Path $projectRoot 'mcp/davinci-resolve/src/server.py'
if (!(Test-Path -LiteralPath $pythonPath) -or !(Test-Path -LiteralPath $serverPath)) {
    throw 'Inicializa el submódulo e instala el entorno Python siguiendo MCP_DAVINCI_GEMINI.md.'
}
& codex mcp add davinci-resolve --env 'RESOLVE_SCRIPT_API=C:/ProgramData/Blackmagic Design/DaVinci Resolve/Support/Developer/Scripting' --env 'RESOLVE_SCRIPT_LIB=C:/Program Files/Blackmagic Design/DaVinci Resolve/fusionscript.dll' --env 'DAVINCI_RESOLVE_MCP_UPDATE_CHECK=0' -- $pythonPath $serverPath
if ($LASTEXITCODE -ne 0) { throw 'No se pudo registrar el MCP en Codex.' }

