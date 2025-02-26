#!/usr/bin/env python3
"""
Installation script for Terminal Controller UVx

This script helps install the Terminal Controller as a UVx package.
"""

import os
import subprocess
import sys
import platform
import json
from pathlib import Path

def check_uvx_installed():
    """Check if UVx is installed in the system"""
    try:
        subprocess.run(
            ["uvx", "--version"], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            check=True
        )
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        return False

def install_uvx():
    """Install UVx if not already installed"""
    print("UVx not found. Installing UVx...")
    
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "uvx"], 
            check=True
        )
        print("UVx installed successfully!")
        return True
    except subprocess.SubprocessError as e:
        print(f"Error installing UVx: {e}")
        return False

def build_package():
    """Build the package using setuptools"""
    print("Building package...")
    
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "build"], 
            check=True
        )
        subprocess.run(
            [sys.executable, "-m", "build", "."], 
            check=True
        )
        print("Package built successfully!")
        return True
    except subprocess.SubprocessError as e:
        print(f"Error building package: {e}")
        return False

def install_package():
    """Install the package using UVx"""
    print("Installing package with UVx...")
    
    try:
        # Find the most recent wheel file in the dist directory
        dist_dir = Path("dist")
        if not dist_dir.exists():
            print("Error: dist directory not found. Build may have failed.")
            return False
            
        wheel_files = list(dist_dir.glob("*.whl"))
        if not wheel_files:
            print("Error: No wheel files found in dist directory.")
            return False
            
        wheel_file = max(wheel_files, key=lambda x: x.stat().st_mtime)
        
        # Install using UVx
        subprocess.run(
            ["uvx", "install", "--file", str(wheel_file)], 
            check=True
        )
        print(f"Package installed successfully with UVx!")
        return True
    except subprocess.SubprocessError as e:
        print(f"Error installing package with UVx: {e}")
        return False

def configure_mcp_client():
    """Configure MCP clients to use terminal-controller"""
    # Determine the configuration location based on the platform
    if platform.system() == "Windows":
        claude_config_path = os.path.expandvars("%APPDATA%\\Claude\\claude_desktop_config.json")
    else:  # macOS
        claude_config_path = os.path.expanduser("~/Library/Application Support/Claude/claude_desktop_config.json")
    
    if os.path.exists(claude_config_path):
        try:
            # Read existing config
            with open(claude_config_path, 'r') as f:
                config = json.load(f)
            
            # Add terminal-controller configuration
            if "mcpServers" not in config:
                config["mcpServers"] = {}
                
            config["mcpServers"]["terminal-controller"] = {
                "command": "uvx",
                "args": ["run", "terminal-controller"],
                "env": {}
            }
            
            # Write updated config
            with open(claude_config_path, 'w') as f:
                json.dump(config, f, indent=2)
            
            print(f"Claude Desktop configured to use terminal-controller!")
            return True
        except Exception as e:
            print(f"Error configuring Claude Desktop: {e}")
            print("You will need to manually configure your MCP client.")
            return False
    else:
        print("Claude Desktop configuration file not found.")
        print("You will need to manually configure your MCP client.")
        return False

def main():
    """Main installation function"""
    print("===== Terminal Controller UVx Installer =====\n")
    
    # Check and install UVx if needed
    if not check_uvx_installed() and not install_uvx():
        print("Failed to install UVx. Installation aborted.")
        return False
    
    # Build the package
    if not build_package():
        print("Failed to build the package. Installation aborted.")
        return False
    
    # Install the package using UVx
    if not install_package():
        print("Failed to install the package with UVx. Installation aborted.")
        return False
    
    # Configure MCP client (if possible)
    configure_mcp_client()
    
    print("\n===== Installation Complete =====")
    print("\nYou can now use Terminal Controller with UVx!")
    print("To run it manually, use: uvx run terminal-controller")
    return True

if __name__ == "__main__":
    main()