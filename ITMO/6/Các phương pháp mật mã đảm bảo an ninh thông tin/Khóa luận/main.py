from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64

# ======== KEY GENERATION ========
def generate_key_pair():
    private = ec.generate_private_key(ec.SECP384R1())
    public = private.public_key()
    return private, public

def generate_shared_key(private_key, peer_public_key):
    shared_secret = private_key.exchange(ec.ECDH(), peer_public_key)
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"onion routing"
    ).derive(shared_secret)
    return base64.urlsafe_b64encode(derived_key)

# ======== INITIALIZE NODES & CLIENT ========
entry_priv, entry_pub = generate_key_pair()
middle_priv, middle_pub = generate_key_pair()
exit_priv, exit_pub = generate_key_pair()
client_priv, client_pub = generate_key_pair()

# ======== CLIENT ESTABLISHES KEYS WITH EACH NODE ========
shared_entry = generate_shared_key(client_priv, entry_pub)
shared_middle = generate_shared_key(client_priv, middle_pub)
shared_exit = generate_shared_key(client_priv, exit_pub)

f_entry = Fernet(shared_entry)
f_middle = Fernet(shared_middle)
f_exit = Fernet(shared_exit)

# ======== MULTI-LAYER ENCRYPTION (CLIENT SIDE) ========
def onion_encrypt(message):
    print(f"\n[Client] Original message: {message}")
    layer1 = f_exit.encrypt(message.encode())
    print(f"[Client] Layer 1 (for Exit): {layer1.decode()[:60]}...")

    layer2 = f_middle.encrypt(layer1)
    print(f"[Client] Layer 2 (for Middle): {layer2.decode()[:60]}...")

    layer3 = f_entry.encrypt(layer2)
    print(f"[Client] Layer 3 (for Entry): {layer3.decode()[:60]}...")
    return layer3

# ======== NODE DECRYPTION ========
def entry_node(packet):
    f = Fernet(generate_shared_key(entry_priv, client_pub))
    decrypted = f.decrypt(packet)
    print(f"\n[Entry Node] Decrypted entry layer, forwarding packet.")
    return decrypted

def middle_node(packet):
    f = Fernet(generate_shared_key(middle_priv, client_pub))
    decrypted = f.decrypt(packet)
    print(f"[Middle Node] Decrypted middle layer, forwarding packet.")
    return decrypted

def exit_node(packet):
    f = Fernet(generate_shared_key(exit_priv, client_pub))
    decrypted = f.decrypt(packet).decode()
    print(f"[Exit Node] Decrypted final layer (Exit).")
    print(f"[Server] Received original message: {decrypted}")
    return decrypted

# ======== SIMULATE FULL PROCESS ========
def simulate_onion_routing():
    message = "Secret data from client to server via Tor network"
    encrypted = onion_encrypt(message)

    p1 = entry_node(encrypted)
    p2 = middle_node(p1)
    p3 = exit_node(p2)

simulate_onion_routing()
