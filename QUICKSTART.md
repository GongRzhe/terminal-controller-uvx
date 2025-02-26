# Terminal Controller UVx - Quick Start Guide

This guide will help you quickly set up and use the Terminal Controller UVx package.

## Installation

### Using UVx (Recommended)

If you have UVx installed, you can directly install Terminal Controller:

```bash
uvx install terminal-controller
```

### Using the Install Script

If you don't have UVx installed, you can use the provided install script:

```bash
python install_uvx.py
```

This script will:
1. Install UVx if it's not already installed
2. Build the package
3. Install it using UVx
4. Configure Claude Desktop (if available)

### Manual Installation

For a manual installation, follow these steps:

1. Build the package:
   ```bash
   pip install build
   python -m build
   ```

2. Install the package:
   ```bash
   pip install dist/*.whl
   ```

## Configuration

### Claude Desktop

If you're using Claude Desktop, you need to add this to your configuration file:

- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

Add the following configuration:

```json
"mcpServers": {
  "terminal-controller": {
    "command": "uvx",
    "args": ["run", "terminal-controller"],
    "env": {}
  }
}
```

### Other MCP Clients

For other MCP clients, refer to their documentation on how to configure UVx packages.

## Usage

Once installed and configured, you can use Terminal Controller with your MCP client.

Here are some examples of what you can do:

- Execute terminal commands:
  ```
  Can you run 'ls -la' to show the files in the current directory?
  ```

- Navigate directories:
  ```
  Change to my Documents folder
  ```

- List files:
  ```
  Show me what files are in my Downloads folder
  ```

- View command history:
  ```
  What commands have been run recently?
  ```

## Troubleshooting

If you're having issues with Terminal Controller:

1. Ensure UVx is properly installed:
   ```bash
   uvx --version
   ```

2. Verify the package is installed with UVx:
   ```bash
   uvx list
   ```

3. Try running the package directly:
   ```bash
   uvx run terminal-controller
   ```

4. Check your MCP client's logs for connection issues

## Need More Help?

Refer to the README.md file for more detailed information or visit the GitHub repository for support.