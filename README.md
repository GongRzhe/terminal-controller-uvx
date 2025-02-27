# Terminal Controller for UVx

A Model Context Protocol (MCP) server that enables secure terminal command execution, directory navigation, and file system operations through a standardized interface, packaged for UVx.

![MCP Server](https://badge.mcpx.dev?type=server)

## Features

- **Command Execution**: Run terminal commands with timeout controls and comprehensive output capture
- **Directory Management**: Navigate and list directory contents with intuitive formatting
- **Security Measures**: Built-in safeguards against dangerous commands and operations
- **Command History**: Track and display recent command executions
- **Cross-Platform Support**: Works on both Windows and UNIX-based systems
- **UVx Integration**: Easily installable via UVx for seamless integration

## Installation

### Using UVx (Recommended)

Install using UVx with a single command:

```bash
uvx install terminal-controller
```

### Manual Installation

For manual installation:

1. Clone this repository:
   ```bash
   git clone https://github.com/GongRzhe/terminal-controller-uvx.git
   cd terminal-controller-uvx
   ```

2. Install the package:
   ```bash
   pip install .
   ```

## Usage

### With UVx

After installation, you can use the Terminal Controller directly with UVx-compatible LLM clients.

### As a Standalone MCP Server

You can also run the Terminal Controller as a standalone MCP server:

```bash
terminal-controller
```

## Client Configuration

### Claude Desktop

Configure Claude Desktop to use Terminal Controller by adding the following to your Claude Desktop configuration:

```json
"terminal-controller": {
  "command": "terminal-controller",
  "args": [],
  "env": {}
}
```

### Other MCP Clients

For other clients, refer to their documentation on how to configure UVx or external MCP servers.

## API Reference

Terminal Controller exposes the following MCP tools:

### `execute_command`

Execute a terminal command and return its results.

**Parameters:**
- `command`: The command line command to execute
- `timeout`: Command timeout in seconds (default: 30)

### `get_command_history`

Get recent command execution history.

**Parameters:**
- `count`: Number of recent commands to return (default: 10)

### `get_current_directory`

Get the current working directory.

### `change_directory`

Change the current working directory.

**Parameters:**
- `path`: Directory path to switch to

### `list_directory`

List files and subdirectories in the specified directory.

**Parameters:**
- `path`: Directory path to list contents (default: current directory)

## Security Considerations

Terminal Controller implements several security measures:

- Timeout controls to prevent long-running commands
- Blacklisting of dangerous commands (rm -rf /, format, mkfs)
- Proper error handling and isolation of command execution
- Access only to the commands and directories specifically granted

## License

MIT