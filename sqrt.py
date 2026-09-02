import streamlit as st
import random
import time

st.set_page_config(
    page_title="Terminal",
    page_icon="💻",
    layout="wide"
)

# Terminal-style CSS
st.markdown("""
<style>
    .stApp {
        background-color: #050505;
        color: #00ff41;
    }

    .terminal {
        background-color: #000000;
        border: 1px solid #00ff41;
        border-radius: 8px;
        padding: 20px;
        font-family: monospace;
        min-height: 500px;
        box-shadow: 0 0 20px rgba(0,255,65,0.15);
    }

    .output {
        color: #00ff41;
        font-family: monospace;
        font-size: 15px;
        white-space: pre-wrap;
    }

    h1 {
        font-family: monospace;
        color: #00ff41 !important;
    }
</style>
""", unsafe_allow_html=True)


# Session state
if "history" not in st.session_state:
    st.session_state.history = [
        "╔════════════════════════════════════════╗",
        "║        CYBER TERMINAL v1.0            ║",
        "║        Simulation Environment         ║",
        "╚════════════════════════════════════════╝",
        "",
        "Type 'help' to see available commands."
    ]


def execute_command(command):

    command = command.lower().strip()

    if command == "help":
        return """
AVAILABLE COMMANDS
------------------
help       Show available commands
status     Show system status
whoami     Show current user
scan       Simulate network scan
connect    Simulate connection
decrypt    Simulate file decryption
clear      Clear terminal
"""

    elif command == "status":
        return """
SYSTEM STATUS
-------------
System       : ONLINE
Firewall     : ACTIVE
Encryption   : AES-256
Connection   : SECURE
Threat Level : LOW
"""

    elif command == "whoami":
        return """
USER INFORMATION
----------------
User     : anonymous
Access   : level_07
Location : UNKNOWN
Identity : [REDACTED]
"""

    elif command == "scan":
        lines = [
            "Initializing network scanner...",
            "Loading modules...",
            "Scanning simulated network..."
        ]

        for line in lines:
            time.sleep(0.4)

        ip = f"192.168.1.{random.randint(2, 254)}"

        return f"""
SCAN COMPLETE
-------------
Target: {ip}

PORT      STATUS
----      ------
22        OPEN
80        OPEN
443       OPEN
8080      FILTERED

No real network traffic was generated.
"""

    elif command == "connect":
        target = f"192.168.1.{random.randint(2,254)}"

        return f"""
CONNECTING TO {target}...

[████████████████████] 100%

Connection established.

SESSION ID: {random.randint(100000,999999)}
ACCESS: SIMULATED
"""

    elif command == "decrypt":
        return """
DECRYPTION MODULE
-----------------
Loading encryption key...
[██████░░░░░░░░░░░░] 32%
[████████████░░░░░░] 67%
[██████████████████] 100%

FILE DECRYPTED

message.txt
-------------------------
"Nice try. This is only a
simulation. 😎"
-------------------------
"""

    elif command == "clear":
        st.session_state.history = []
        return ""

    elif command == "":
        return ""

    else:
        return f"Command not found: {command}\nType 'help' for available commands."


st.title("💻 CYBER TERMINAL")

# Display terminal
terminal_text = "\n".join(st.session_state.history)

st.markdown(
    f'<div class="terminal"><div class="output">{terminal_text}</div></div>',
    unsafe_allow_html=True
)

st.write("")

# Command input
command = st.text_input(
    "terminal",
    placeholder="Enter command...",
    label_visibility="collapsed"
)

if st.button("EXECUTE", use_container_width=True):

    if command:

        st.session_state.history.append(
            f"root@cyber:~$ {command}"
        )

        result = execute_command(command)

        if result:
            st.session_state.history.extend(
                result.strip("\n").split("\n")
            )

        st.rerun()
