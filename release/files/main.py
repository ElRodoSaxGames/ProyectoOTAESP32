# import ujson, time

# VERSION = "1.0.0"

# def commit_ok(bank, version):
#     with open("state.json", "r") as f:
#         st = ujson.load(f)

#     # Solo commit si este bank era el pending
#     if st.get("pending_bank") == bank and st.get("pending_version") == version:
#         st["active_bank"] = bank
#         st["active_version"] = version
#         st["pending_bank"] = None
#         st["pending_version"] = None
#         st["boot_try"] = 0
#         with open("state.json", "w") as f:
#             ujson.dump(st, f)

# # Commit temprano: si tu app llega aquí, al menos arrancó bien.
# # (Mejor: haz commit después de validar WiFi/sensores si quieres más seguridad)
# commit_ok(globals().get("BANK", "?"), VERSION)

# from app.iot import loop
# loop()

import ujson

VERSION = "1.0.1"  # súbelo cada vez que cambies release

def commit_ok(bank, version):
    with open("state.json", "r") as f:
        st = ujson.load(f)

    if st.get("pending_bank") == bank and st.get("pending_version") == version:
        st["active_bank"] = bank
        st["active_version"] = version
        st["pending_bank"] = None
        st["pending_version"] = None
        st["boot_try"] = 0
        with open("state.json", "w") as f:
            ujson.dump(st, f)

# Si tu app ya arrancó, hacemos commit
commit_ok(globals().get("BANK", "?"), VERSION)

from app.blink import run
run()
