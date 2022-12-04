# s="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
s="map"
for c in s:
    if ord('a') <= ord(c) <= ord('z'):
        print(chr(((ord(c) - ord('a') + 2) % 26) + ord('a')), end="")
    else:
        print(c, end="")