"""
Utility module for finding available ports.
"""

import socket
from typing import Optional


def find_free_port(start_port: int = 7860, max_attempts: int = 100) -> int:
    """
    Find an available port starting from the given port.
    
    Args:
        start_port: Port to start searching from (default: 7860)
        max_attempts: Maximum number of ports to try (default: 100)
    
    Returns:
        Available port number
        
    Raises:
        RuntimeError: If no available port is found within the range
    """
    for port in range(start_port, start_port + max_attempts):
        if _is_port_available(port):
            return port
    
    raise RuntimeError(
        f"No available port found in range {start_port}-{start_port + max_attempts - 1}"
    )


def _is_port_available(port: int) -> bool:
    """
    Check if a port is available for binding.
    
    Args:
        port: Port number to check
        
    Returns:
        True if port is available, False otherwise
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind(('localhost', port))
            return True
    except socket.error:
        return False


def get_available_ports(
    start_port: int = 7860, 
    count: int = 2, 
    max_attempts: int = 100
) -> list[int]:
    """
    Get multiple available ports.
    
    Args:
        start_port: Port to start searching from
        count: Number of ports to find
        max_attempts: Maximum number of ports to try per port
        
    Returns:
        List of available port numbers
        
    Raises:
        RuntimeError: If enough available ports are not found
    """
    available_ports = []
    current_port = start_port
    
    while len(available_ports) < count and current_port < start_port + max_attempts:
        if _is_port_available(current_port):
            available_ports.append(current_port)
        current_port += 1
    
    if len(available_ports) < count:
        raise RuntimeError(
            f"Could not find {count} available ports in range {start_port}-{current_port - 1}"
        )
    
    return available_ports