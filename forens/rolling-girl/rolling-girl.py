# DO NOT UNZIP INFINIROLL
# DO NOT UNZIP INFINIROLL
# DO NOT UNZIP INFINIROLL
# DO NOT UNZIP INFINIROLL

# SERIOUSLY
# SERIOUSLY
# SERIOUSLY
# SERIOUSLY

# IT IS FUNCTIONALLY A ZIP BOMB
# IT IS FUNCTIONALLY A ZIP BOMB
# IT IS FUNCTIONALLY A ZIP BOMB
# IT IS FUNCTIONALLY A ZIP BOMB

# YOUR PC WILL DIE
# YOUR PC WILL DIE
# YOUR PC WILL DIE
# YOUR PC WILL DIE

# YOU HAVE BEEN WARNED IT IS NO LONGER OUR RESPONSIBILITY IF YOU UNZIP THE FILE
# YOU HAVE BEEN WARNED IT IS NO LONGER OUR RESPONSIBILITY IF YOU UNZIP THE FILE
# YOU HAVE BEEN WARNED IT IS NO LONGER OUR RESPONSIBILITY IF YOU UNZIP THE FILE
# YOU HAVE BEEN WARNED IT IS NO LONGER OUR RESPONSIBILITY IF YOU UNZIP THE FILE

import gzip
from tqdm import tqdm
import random
import zstandard as zstd

gif = bytearray(open('rolling-girl.gif', 'rb').read())
flag_gif = bytearray(open('flag.gif', 'rb').read())
# flag is just the gif with the flag overlaid
# no steganography, so don't try it!

# this is just to merge the two gifs' color palettes together
# it's not challenge relevant
flag_header = flag_gif[:0x320]
normal_header = gif[:0x320]
header = bytearray()
for a, b in zip(flag_header, normal_header):
    if a == b:
        header.extend(a.to_bytes())
    if a != b:
        if a == 0:
            header.extend(b.to_bytes())
        else:
            header.extend(a.to_bytes())
    
images = gif[0x320:-1]
flag_images = flag_gif[0x320:-1]
trailer = b';'

iterations = 1000000
flag_iteration = random.randint(0, 5000) # you're welcome

output_file = 'infiniroll.gif.zst'

cctx = zstd.ZstdCompressor()
with open(output_file, 'wb') as fh:
    with cctx.stream_writer(fh) as compressor:
        compressor.write(header)
        for i in tqdm(range(1, iterations)):
            compressor.write(images)
            if i == flag_iteration:
                print('Writing flag...')
                compressor.write(flag_images)
        compressor.write(trailer)